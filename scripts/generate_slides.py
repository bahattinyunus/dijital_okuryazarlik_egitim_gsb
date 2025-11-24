#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSB Dijital Okuryazarlık Eğitimi - Toplu Marp Slayt Dönüştürücü
================================================================

Bu script, ders klasörlerindeki Marp uyumlu Markdown slaytlarını
toplu olarak HTML / PDF / PPTX formatlarına dönüştürür.

Özellikler:
- Klasör ağacını tarayarak Marp dosyalarını bulma (front-matter: `marp: true`)
- Varsayılan dosya adı: `slayt_marp.md` (override edilebilir)
- Marp CLI ile dönüştürme (kurulu değilse bilgilendirir)
- Basit bir HTML fallback üreticisi (Marp yoksa en temel görünümle)
- Çıkışları kök /dist/slides altına, kaynak hiyerarşisini koruyarak yazma
- Renkli loglar, özet rapor ve dry-run desteği

Kurulum:
- Python paketleri (requirements.txt): click, colorama, tqdm, markdown, pymdown-extensions, pyyaml
- Marp CLI (global, Node.js gerekir): npm i -g @marp-team/marp-cli

Kullanım:
  python scripts/generate_slides.py --help

Örnekler:
  # Varsayılan ayarlarla (HTML üretir)
  python scripts/generate_slides.py

  # PDF + HTML üret
  python scripts/generate_slides.py --formats html --formats pdf

  # Sadece belirli dosya adına göre tara
  python scripts/generate_slides.py --pattern slayt_marp.md

  # Tüm .md dosyalarını tara ve front-matter'da marp: true olanları dönüştür
  python scripts/generate_slides.py --pattern ""

  # Çıktı klasörünü değiştir
  python scripts/generate_slides.py --output-root ../dist/my_slides
"""

from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import click
except ImportError:  # pragma: no cover
    print("Bu script 'click' paketine ihtiyaç duyar. Lütfen: pip install click")
    sys.exit(1)

try:
    from colorama import Fore, Style
    from colorama import init as colorama_init
except ImportError:  # pragma: no cover

    class Dummy:
        RESET_ALL = ""

    class ForeDummy:
        GREEN = CYAN = YELLOW = RED = MAGENTA = BLUE = ""

    class StyleDummy:
        BRIGHT = NORMAL = ""

    Fore = ForeDummy()
    Style = StyleDummy()

    def colorama_init():  # type: ignore
        pass


try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover

    def tqdm(iterable, **kwargs):
        return iterable


# Fallback HTML üretimi için:
try:
    import markdown as md
except ImportError:
    md = None  # Fallback çalışmayabilir, uyaracağız.

try:
    import yaml
except ImportError:
    yaml = None  # Front-matter için alternatif string taraması yaparız.


colorama_init()


# -----------------------------
# Yardımcı Fonksiyonlar
# -----------------------------


def project_root() -> Path:
    # scripts/ dizininden iki kademe yukarı gsb_eğitim kökü
    return Path(__file__).resolve().parent.parent


def default_input_root() -> Path:
    return project_root() / "ders_notlari"


def default_output_root() -> Path:
    return project_root() / "dist" / "slides"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def find_markdown_files(root: Path, pattern: str) -> List[Path]:
    """
    pattern:
      - 'slayt_marp.md' gibi bir dosya adı: sadece bu adı arar
      - '' (boş) verilirse: tüm *.md dosyalarını arar
    """
    if not root.exists():
        return []
    if pattern and pattern.strip():
        return sorted(root.rglob(pattern))
    # pattern boş ise tüm md dosyalarını tara
    return sorted(root.rglob("*.md"))


def extract_front_matter(text: str) -> Tuple[Dict, str]:
    """
    YAML front-matter'ı varsa ayıklar. Yoksa boş dict döner.
    Dönüş:
      (front_matter_dict, content_without_front_matter)
    """
    if not text.startswith("---\n"):
        return {}, text

    end_idx = text.find("\n---", 4)
    if end_idx == -1:
        return {}, text

    yaml_block = text[4:end_idx]
    rest = text[end_idx + 4 :]
    if yaml:
        try:
            data = yaml.safe_load(yaml_block) or {}
            if not isinstance(data, dict):
                data = {}
        except Exception:
            data = {}
    else:
        # YAML yoksa, kaba bir anahtar taraması yapalım
        data = {}
        for line in yaml_block.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip()
    return data, rest.lstrip("\n")


def is_marp_markdown(path: Path) -> bool:
    """
    Dosyanın Marp içerip içermediğini kontrol eder:
    - Front-matter'da 'marp: true'
    - Metin içinde 'marp: true' benzeri ilk 50 satırda geçen ifade
    """
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False

    fm, _ = extract_front_matter(text)
    if isinstance(fm.get("marp", None), bool) and fm.get("marp"):
        return True
    if isinstance(fm.get("marp", None), str) and fm.get("marp", "").lower() == "true":
        return True

    # front-matter yoksa, ilk 50 satırda 'marp:' ara
    lines = text.splitlines()[:50]
    for ln in lines:
        if re.search(r"\bmarp\s*:\s*true\b", ln.strip(), re.IGNORECASE):
            return True
    return False


def which_marp() -> Optional[str]:
    return shutil.which("marp")


def build_output_path(
    input_root: Path, input_path: Path, output_root_dir: Path, fmt: str
) -> Path:
    """
    Kaynak dosyanın input_root'a göre göreli yolunu koruyarak out path üret.
    Örn:
      input_root = .../ders_notlari
      input_path = .../ders_notlari/03_google_slides/slayt_marp.md
      output_root_dir = .../dist/slides
      fmt=html
    Çıktı:
      .../dist/slides/03_google_slides/slayt_marp.html
    """
    rel = input_path.relative_to(input_root)
    stem = rel.stem
    parent = rel.parent
    return output_root_dir / parent / f"{stem}.{fmt}"


def needs_build(src: Path, dst: Path) -> bool:
    if not dst.exists():
        return True
    try:
        return src.stat().st_mtime > dst.stat().st_mtime
    except Exception:
        return True


def run_subprocess(cmd: List[str]) -> Tuple[int, str, str]:
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    out, err = proc.communicate()
    return proc.returncode, out, err


def render_with_marp_cli(
    marp_bin: str,
    input_path: Path,
    output_path: Path,
    fmt: str,
    theme: Optional[str],
    allow_local_files: bool = True,
    extra_args: Optional[List[str]] = None,
) -> Tuple[bool, str]:
    args = [marp_bin, str(input_path)]
    if fmt == "html":
        args.append("--html")
    elif fmt == "pdf":
        args.append("--pdf")
    elif fmt == "pptx":
        args.append("--pptx")
    else:
        return False, f"Desteklenmeyen format: {fmt}"

    if allow_local_files:
        args.append("--allow-local-files")

    if theme:
        args.extend(["--theme", theme])

    args.extend(["-o", str(output_path)])

    if extra_args:
        args.extend(extra_args)

    code, out, err = run_subprocess(args)
    if code == 0:
        return True, out.strip()
    return False, (err.strip() or out.strip() or f"Marp dönüşüm hatası (kod={code})")


# -----------------------------
# Fallback HTML Üretici
# -----------------------------

FALLBACK_CSS = """
/* Çok basit bir fallback slayt görünümü */
body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; background: #111827; color: #111; }
.deck { display: flex; flex-direction: column; gap: 24px; padding: 24px; background: #111827; min-height: 100vh; }
.slide { background: #ffffff; border-radius: 16px; padding: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); max-width: 1280px; margin: 0 auto; }
.slide h1, .slide h2, .slide h3 { color: #1F2937; }
.meta { font-size: 14px; color: #6B7280; margin: 8px 0 0 2px; }
.footer { text-align: center; padding: 16px; color: #D1D5DB; font-size: 12px; }
kbd { background: #F3F4F6; border: 1px solid #E5E7EB; border-radius: 6px; padding: 2px 6px; }
"""

FALLBACK_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="deck">
{slides}
</div>
<div class="footer">Fallback görünümü — Marp CLI yüklü değilse basit HTML üretildi.</div>
</body>
</html>
"""


def fallback_split_slides(markdown_text: str) -> List[str]:
    """
    Çok basit slayt bölücü: Üç çizgi (---) ile ayrılmış bölümleri slayt kabul eder.
    Marp özelliklerini desteklemez; sadece acil durum çıktısı üretir.
    """
    # Front-matter kaldır
    fm, content = extract_front_matter(markdown_text)
    parts = re.split(r"(?m)^\s*---\s*$", content.strip())
    return [p.strip() for p in parts if p.strip()]


def fallback_markdown_to_html(md_text: str) -> str:
    if md is None:
        # markdown paketi yoksa, basit kaçış yap
        esc = md_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return "<pre>" + esc + "</pre>"
    return md.markdown(
        md_text,
        extensions=[
            "extra",
            "toc",
            "sane_lists",
            "admonition",
            "tables",
            "pymdownx.highlight",
            "pymdownx.superfences",
        ],
        output_format="html5",
    )


def render_fallback_html(input_path: Path, output_path: Path) -> None:
    raw = input_path.read_text(encoding="utf-8", errors="ignore")
    fm, _content_ignored = extract_front_matter(raw)
    title = fm.get("title") if isinstance(fm, dict) else None
    if not title:
        title = input_path.stem

    slides_md = fallback_split_slides(raw)
    slides_html = []
    for idx, slide_md in enumerate(slides_md, 1):
        body_html = fallback_markdown_to_html(slide_md)
        slides_html.append(
            f'<section class="slide"><div class="meta">Slayt {idx}</div>{body_html}</section>'
        )

    html = FALLBACK_HTML_TEMPLATE.format(
        title=title, css=FALLBACK_CSS, slides="\n".join(slides_html)
    )
    write_text(output_path, html)


# -----------------------------
# CLI
# -----------------------------


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--input-root",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=lambda: default_input_root(),
    help="Kaynak ders kökü (varsayılan: ../ders_notlari)",
)
@click.option(
    "--output-root",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=lambda: default_output_root(),
    help="Çıktı kökü (varsayılan: ../dist/slides)",
)
@click.option(
    "--pattern",
    type=str,
    default="slayt_marp.md",
    help='Aranacak dosya adı. Boş "" verilirse tüm *.md dosyalarında front-matter "marp: true" aranır.',
)
@click.option(
    "--formats",
    "formats_",
    type=click.Choice(["html", "pdf", "pptx"], case_sensitive=False),
    multiple=True,
    default=("html",),
    help="Üretilecek formatlar (çoklu seçim mümkün). Varsayılan: html",
)
@click.option(
    "--force/--no-force",
    default=False,
    help="Var olan güncel çıktıları da yeniden üret.",
)
@click.option(
    "--theme",
    type=str,
    default=None,
    help="Marp tema dosyası (opsiyonel). Örn: ./themes/custom.css",
)
@click.option(
    "--dry-run/--no-dry-run",
    default=False,
    help="Dönüşüm yapmadan yapılacak işlemleri göster.",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Detaylı loglar.",
)
def main(
    input_root: Path,
    output_root: Path,
    pattern: str,
    formats_: Tuple[str, ...],
    force: bool,
    theme: Optional[str],
    dry_run: bool,
    verbose: bool,
) -> None:
    """
    Toplu Marp slayt dönüştürücü.

    Notlar:
    - Marp CLI bulunursa onu kullanır. Bulunamazsa HTML için basit fallback üretir.
    - PDF ve PPTX için Marp CLI zorunludur.
    """
    print(Style.BRIGHT + f"\n🚀 GSB Marp Slayt Dönüştürücü" + Style.RESET_ALL)
    print(
        f"Giriş: {Fore.CYAN}{input_root}{Fore.RESET}  →  Çıkış: {Fore.CYAN}{output_root}{Fore.RESET}"
    )
    print(f"Arama deseni: {Fore.YELLOW}{pattern or '[tüm *.md]'}{Fore.RESET}")
    print(f"Formatlar: {Fore.GREEN}{', '.join(formats_)}{Fore.RESET}")
    if theme:
        print(f"Tema: {Fore.MAGENTA}{theme}{Fore.RESET}")
    if dry_run:
        print(f"{Fore.YELLOW}Dry-run etkin: Dosya üretimi yapılmayacak.{Fore.RESET}")

    candidates = find_markdown_files(input_root, pattern)
    if not candidates:
        print(Fore.RED + "Hiç kaynak dosya bulunamadı." + Fore.RESET)
        sys.exit(1)

    # Filtre: pattern boşsa marp: true içerenleri al
    if not pattern.strip():
        marp_candidates = [p for p in candidates if is_marp_markdown(p)]
    else:
        # pattern belirtilmişse yine de marp kontrolü yapalım,
        # ama uyarı verip dönüştürelim (çıktı olmayabilir).
        marp_candidates = []
        for p in candidates:
            if is_marp_markdown(p):
                marp_candidates.append(p)
            else:
                print(
                    Fore.YELLOW
                    + f"Uyarı: Marp front-matter bulunamadı: {p}"
                    + Fore.RESET
                )
                marp_candidates.append(p)  # Yine de dönüştürmeyi deneriz.

    if not marp_candidates:
        print(Fore.RED + "Marp uyumlu dosya bulunamadı." + Fore.RESET)
        sys.exit(1)

    marp_bin = which_marp()
    if marp_bin:
        print(Fore.GREEN + f"Marp CLI bulundu: {marp_bin}" + Fore.RESET)
    else:
        print(
            Fore.YELLOW
            + "Marp CLI bulunamadı. HTML için basit fallback üretilecektir. PDF/PPTX üretilemez.\n"
            "Kurulum için: npm i -g @marp-team/marp-cli" + Fore.RESET
        )

    total = 0
    built = 0
    skipped = 0
    failed = 0
    tasks: List[Tuple[Path, str, Path]] = []

    for src in marp_candidates:
        for fmt in formats_:
            out_path = build_output_path(input_root, src, output_root, fmt)
            tasks.append((src, fmt, out_path))

    for src, fmt, out_path in tqdm(tasks, desc="Dönüştürülüyor", unit="dosya"):
        total += 1
        do_build = force or needs_build(src, out_path)
        if not do_build:
            skipped += 1
            if verbose:
                print(Fore.BLUE + f"Atlandı (güncel): {out_path}" + Fore.RESET)
            continue

        if dry_run:
            built += 1
            print(Fore.CYAN + f"[DRY] {src} -> {out_path}" + Fore.RESET)
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)

        if marp_bin:
            # Marp ile üret
            ok, msg = render_with_marp_cli(
                marp_bin=marp_bin,
                input_path=src,
                output_path=out_path,
                fmt=fmt.lower(),
                theme=theme,
                allow_local_files=True,
                extra_args=None,
            )
            if ok:
                built += 1
                if verbose:
                    print(Fore.GREEN + f"Üretildi: {out_path}" + Fore.RESET)
            else:
                failed += 1
                print(Fore.RED + f"Hata ({src.name} -> {fmt}): {msg}" + Fore.RESET)
        else:
            # Fallback sadece HTML
            if fmt.lower() != "html":
                failed += 1
                print(
                    Fore.RED
                    + f"Hata: Marp CLI olmadan {fmt.upper()} üretilemez: {src}"
                    + Fore.RESET
                )
                continue
            try:
                render_fallback_html(src, out_path)
                built += 1
                if verbose:
                    print(
                        Fore.GREEN + f"Fallback HTML üretildi: {out_path}" + Fore.RESET
                    )
            except Exception as e:
                failed += 1
                print(Fore.RED + f"Fallback hatası: {src} -> {e}" + Fore.RESET)

    # Özet
    print("\n" + Style.BRIGHT + "📊 Özet" + Style.RESET_ALL)
    print(f"Toplam:   {total}")
    print(Fore.GREEN + f"Üretildi: {built}" + Fore.RESET)
    print(Fore.BLUE + f"Atlandı:  {skipped}" + Fore.RESET)
    if failed:
        print(Fore.RED + f"Başarısız: {failed}" + Fore.RESET)

    # Çıkış kodu
    if failed > 0:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()

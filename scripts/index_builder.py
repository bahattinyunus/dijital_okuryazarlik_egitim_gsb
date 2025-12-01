#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INDEX.md üreticisi
------------------

Bu yardımcı komut, `ders_notlari` dizinini tarayarak her dersin
özetini çıkarır ve kök dizindeki `INDEX.md` dosyasını otomatik olarak
günceller. Böylece yeni ders eklendiğinde ya da mevcut içerikler
güncellendiğinde dizini manuel düzenlemek gerekmez.

Kullanım:
    python scripts/index_builder.py --write

Opsiyonlar:
    --lessons-root   : Ders klasörlerinin bulunduğu dizin (varsayılan: ../ders_notlari)
    --examples-root  : Örnek çalışmaların bulunduğu dizin (varsayılan: ../ornek_calisma)
    --output         : Üretilen INDEX dosyasının yolu (varsayılan: ../INDEX.md)
    --check          : Dosyaya yazmadan özet çıktısını gösterir
"""

from __future__ import annotations

import argparse
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class LessonSummary:
    slug: str
    title: str
    plan_path: Optional[Path]
    slide_path: Optional[Path]
    duration: Optional[str] = None
    objectives: List[str] = field(default_factory=list)
    example_path: Optional[Path] = None
    notes: List[str] = field(default_factory=list)


def parse_markdown_plan(path: Path) -> LessonSummary:
    """
    Ders planı markdown dosyasından başlık, süre ve amaçlar gibi
    temel bilgileri çıkarır.
    """
    slug = path.parent.name
    title = f"{slug} dersi"
    duration = None
    objectives: List[str] = []

    lines = path.read_text(encoding="utf-8").splitlines()

    current_heading: Optional[str] = None
    buffer: List[str] = []

    def flush_objectives():
        nonlocal objectives
        if current_heading and "ders amacı" in current_heading.lower():
            cleaned = [line.lstrip("-* ").strip() for line in buffer if line.strip()]
            # İlk 4 madde yeterli; daha fazlası tabloyu doldurur
            objectives = cleaned[:4]

    def flush_duration():
        nonlocal duration
        if duration is not None:
            return
        if current_heading and "süre" in current_heading.lower():
            for line in buffer:
                stripped = line.strip()
                if stripped:
                    duration = stripped
                    return

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            # İlk H1 başlığı dersin tam başlığıdır
            if title == f"{slug} dersi":
                title = stripped.lstrip("# ").strip()
            continue

        if stripped.startswith("## "):
            flush_objectives()
            flush_duration()
            current_heading = stripped.lstrip("# ").strip()
            buffer = []
            continue

        buffer.append(line)

    flush_objectives()
    flush_duration()

    return LessonSummary(
        slug=slug,
        title=title,
        plan_path=path,
        slide_path=path.parent / "slayt_marp.md",
        duration=duration,
        objectives=objectives,
    )


def discover_lessons(lessons_root: Path) -> List[LessonSummary]:
    summaries: List[LessonSummary] = []
    for lesson_dir in sorted(lessons_root.iterdir()):
        if not lesson_dir.is_dir():
            continue
        plan_path = lesson_dir / "ders_plani.md"
        if plan_path.exists():
            summary = parse_markdown_plan(plan_path)
        else:
            summary = LessonSummary(
                slug=lesson_dir.name,
                title=lesson_dir.name.replace("_", " ").title(),
                plan_path=None,
                slide_path=lesson_dir / "slayt_marp.md",
            )
            summary.notes.append("Ders planı eksik")

        if not summary.slide_path.exists():
            summary.notes.append("Slayt dosyası eksik")

        summaries.append(summary)
    return summaries


def map_examples(summary: LessonSummary, examples_root: Path) -> None:
    """
    Bazı dersler için örnek çalışma klasörlerini heuristik olarak eşleştirir.
    """
    example_map = {
        "01_canva": "canva_ornekleri/proje_onerileri.md",
        "02_google_docs": "google_workspace/dokuman_sablonlari.md",
        "03_google_slides": "google_workspace/dokuman_sablonlari.md",
        "04_google_forms": "google_workspace/dokuman_sablonlari.md",
        "05_trello": "proje_yonetimi/kanban_sablonlari.md",
        "06_notion": "proje_yonetimi/kanban_sablonlari.md",
        "07_google_drive": "google_workspace/dokuman_sablonlari.md",
        "08_siber_guvenlik": "video_ornekleri/capcut_proje_rehberi.md",
        "09_yapay_zeka": "yapay_zeka_lab/ai_proje_atolyesi.md",
        "10_chatgpt": None,
        "11_capcut": "video_ornekleri/capcut_proje_rehberi.md",
        "12_sosyal_medya_etik": None,
    }

    rel = example_map.get(summary.slug)
    if rel:
        candidate = examples_root / rel
        if candidate.exists():
            summary.example_path = candidate


def build_index_markdown(lessons: List[LessonSummary], project_root: Path) -> str:
    intro = textwrap.dedent(
        """\
        <!-- NOTE: Bu dosya scripts/index_builder.py tarafından otomatik üretilmiştir. -->
        # GSB Dijital Okuryazarlık Eğitimi - İçerik Dizini

        Bu dosya, `scripts/index_builder.py` komutu kullanılarak ders klasörlerinden otomatik üretilmiştir.
        Yeni bir ders eklendiğinde veya içerik güncellendiğinde aşağıdaki komutu çalıştırmanız yeterlidir:

        ```bash
        python scripts/index_builder.py --write
        ```
        """
    )

    table_header = (
        "| Ders | Süre | Plan | Slayt | Özet |\n"
        "|------|------|------|-------|------|\n"
    )

    table_rows = []
    for lesson in lessons:
        duration = lesson.duration or "`-`"
        plan_link = (
            f"[ders_plani.md]({lesson.plan_path.relative_to(project_root).as_posix()})"
            if lesson.plan_path and lesson.plan_path.exists()
            else "`Eksik`"
        )
        slide_link = (
            f"[slayt_marp.md]({lesson.slide_path.relative_to(project_root).as_posix()})"
            if lesson.slide_path.exists()
            else "`Eksik`"
        )
        summary_text = ", ".join(lesson.objectives[:3]) if lesson.objectives else "Açıklama bekleniyor"
        table_rows.append(f"| {lesson.title} | {duration} | {plan_link} | {slide_link} | {summary_text} |")

    details_sections = []
    for lesson in lessons:
        sections = [f"## {lesson.title}", ""]

        if lesson.plan_path and lesson.plan_path.exists():
            rel_plan = lesson.plan_path.relative_to(project_root).as_posix()
            sections.append(f"- 📄 Ders Planı: [`{rel_plan}`]({rel_plan})")
        else:
            sections.append("- 📄 Ders Planı: **Eksik**")

        if lesson.slide_path.exists():
            rel_slide = lesson.slide_path.relative_to(project_root).as_posix()
            sections.append(f"- 🖥️ Slayt: [`{rel_slide}`]({rel_slide})")
        else:
            sections.append("- 🖥️ Slayt: **Eksik**")

        if lesson.example_path:
            rel_example = lesson.example_path.relative_to(project_root).as_posix()
            sections.append(f"- 🧪 Örnek Çalışma: [`{rel_example}`]({rel_example})")

        if lesson.duration:
            sections.append(f"- ⏰ Süre: {lesson.duration}")

        if lesson.objectives:
            sections.append("- 🎯 Hedefler:")
            for obj in lesson.objectives:
                sections.append(f"  - {obj}")

        if lesson.notes:
            sections.append("- ⚠️ Notlar:")
            for note in lesson.notes:
                sections.append(f"  - {note}")

        sections.append("")
        details_sections.append("\n".join(sections))

    return "\n".join(
        [
            intro.strip(),
            "",
            "## Derslere Hızlı Bakış",
            "",
            table_header + "\n".join(table_rows),
            "",
            "## Ayrıntılı İçerikler",
            "",
            "\n".join(details_sections).strip(),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="INDEX.md otomatik üreticisi")
    parser.add_argument(
        "--lessons-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "ders_notlari",
    )
    parser.add_argument(
        "--examples-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "ornek_calisma",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "INDEX.md",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Dosyaya yazmadan üretilecek metni stdout'a bas",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Oluşturulan içeriği hedef dosyaya kaydet",
    )

    args = parser.parse_args()

    lessons = discover_lessons(args.lessons_root)
    for lesson in lessons:
        map_examples(lesson, args.examples_root)

    project_root = Path(__file__).resolve().parent.parent
    markdown = build_index_markdown(lessons, project_root)

    if args.check or not args.write:
        print(markdown)

    if args.write:
        args.output.write_text(markdown + "\n", encoding="utf-8")
        print(f"✅ INDEX güncellendi: {args.output}")


if __name__ == "__main__":
    main()


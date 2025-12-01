#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İçerik Raporlayıcı
------------------

`ders_notlari/` dizinindeki her ders için içerik bütünlüğünü analiz eder,
eksik dosyaları raporlar ve istenirse JSON çıktı üretir.

Örnekler:
    python scripts/content_report.py
    python scripts/content_report.py --json-out dist/content_report.json
"""

from __future__ import annotations

import argparse
import json
import textwrap
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class LessonReport:
    slug: str
    title: str
    has_plan: bool
    has_slide_md: bool
    has_slide_exports: Dict[str, bool]
    has_examples: bool
    duration: Optional[str]
    objectives: List[str]
    plan_word_count: int
    notes: List[str]

    def completeness_score(self) -> int:
        """0-4 arası tamamlanma puanı."""
        score = 0
        score += 1 if self.has_plan else 0
        score += 1 if self.has_slide_md else 0
        score += 1 if any(self.has_slide_exports.values()) else 0
        score += 1 if self.has_examples else 0
        return score


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_duration_and_objectives(text: str) -> tuple[Optional[str], List[str]]:
    duration = None
    objectives: List[str] = []
    current = None
    buffer: List[str] = []

    def flush():
        nonlocal duration, objectives, current
        if current is None:
            return
        label = current.lower()
        cleaned = [line.lstrip("-* ").strip() for line in buffer if line.strip()]
        if "süre" in label and duration is None and cleaned:
            duration = cleaned[0]
        if "ders amacı" in label and not objectives:
            objectives = cleaned[:4]

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            flush()
            current = stripped.lstrip("# ").strip()
            buffer = []
        else:
            buffer.append(line)
    flush()
    return duration, objectives


def discover_lessons(root: Path, examples_root: Path, dist_root: Path) -> List[LessonReport]:
    lessons: List[LessonReport] = []
    for lesson_dir in sorted(root.iterdir()):
        if not lesson_dir.is_dir():
            continue
        slug = lesson_dir.name
        plan_path = lesson_dir / "ders_plani.md"
        slide_md = lesson_dir / "slayt_marp.md"

        has_plan = plan_path.exists()
        has_slide_md = slide_md.exists()

        duration = None
        objectives: List[str] = []
        word_count = 0
        notes: List[str] = []
        title = slug.replace("_", " ").title()

        if has_plan:
            text = read_markdown(plan_path)
            duration, objectives = extract_duration_and_objectives(text)
            word_count = len(text.split())
            first_line = text.splitlines()[0].strip()
            if first_line.startswith("#"):
                title = first_line.lstrip("# ").strip()
        else:
            notes.append("Ders planı eksik")

        if not has_slide_md:
            notes.append("Marp slaytı eksik")

        slide_exports = {}
        dist_dir = dist_root / slug
        for fmt in ("html", "pdf", "pptx"):
            slide_exports[fmt] = (dist_dir / f"slayt_marp.{fmt}").exists()
        if not any(slide_exports.values()):
            notes.append("dist/slides çıktıları bulunamadı")

        example_path = guess_example(slug, examples_root)
        has_examples = example_path is not None
        if not has_examples:
            notes.append("Örnek çalışma eşleşmedi")

        lessons.append(
            LessonReport(
                slug=slug,
                title=title,
                has_plan=has_plan,
                has_slide_md=has_slide_md,
                has_slide_exports=slide_exports,
                has_examples=has_examples,
                duration=duration,
                objectives=objectives,
                plan_word_count=word_count,
                notes=notes,
            )
        )
    return lessons


def guess_example(slug: str, examples_root: Path) -> Optional[Path]:
    mapping = {
        "01_canva": "canva_ornekleri/proje_onerileri.md",
        "02_google_docs": "google_workspace/dokuman_sablonlari.md",
        "03_google_slides": "google_workspace/dokuman_sablonlari.md",
        "04_google_forms": "google_workspace/dokuman_sablonlari.md",
        "05_trello": "proje_yonetimi/kanban_sablonlari.md",
        "06_notion": "proje_yonetimi/kanban_sablonlari.md",
        "07_google_drive": "google_workspace/dokuman_sablonlari.md",
        "09_yapay_zeka": "yapay_zeka_lab/ai_proje_atolyesi.md",
        "11_capcut": "video_ornekleri/capcut_proje_rehberi.md",
    }
    rel = mapping.get(slug)
    if not rel:
        return None
    path = examples_root / rel
    return path if path.exists() else None


def human_table(lessons: List[LessonReport]) -> str:
    headers = ["Ders", "Plan", "Slayt", "Çıktı", "Örnek", "Kelime"]
    lines = [" | ".join(headers), " | ".join("---" for _ in headers)]
    for report in lessons:
        lines.append(
            " | ".join(
                [
                    report.slug,
                    "✅" if report.has_plan else "❌",
                    "✅" if report.has_slide_md else "❌",
                    "✅" if any(report.has_slide_exports.values()) else "❌",
                    "✅" if report.has_examples else "❌",
                    str(report.plan_word_count),
                ]
            )
        )
    return "\n".join(lines)


def summarize(lessons: List[LessonReport]) -> Dict[str, int]:
    total = len(lessons)
    complete = sum(1 for l in lessons if l.completeness_score() == 4)
    with_plan = sum(1 for l in lessons if l.has_plan)
    with_slide = sum(1 for l in lessons if l.has_slide_md)
    with_exports = sum(1 for l in lessons if any(l.has_slide_exports.values()))
    return {
        "total_lessons": total,
        "complete_lessons": complete,
        "plan_coverage": with_plan,
        "slide_markdown_coverage": with_slide,
        "export_coverage": with_exports,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Ders içerik raporu")
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
        "--dist-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "dist" / "slides",
    )
    parser.add_argument("--json-out", type=Path, help="Raporu JSON olarak kaydet")
    args = parser.parse_args()

    lessons = discover_lessons(args.lessons_root, args.examples_root, args.dist_root)

    stats = summarize(lessons)
    print(textwrap.dedent(
        f"""
        📊 Ders İçerik Raporu
        --------------------
        Toplam ders: {stats['total_lessons']}
        Tamamı hazır ders: {stats['complete_lessons']}
        Ders planı bulunan: {stats['plan_coverage']}
        Slayt markdown bulunan: {stats['slide_markdown_coverage']}
        dist çıktısı bulunan: {stats['export_coverage']}
        """
    ).strip())

    print("\n" + human_table(lessons))

    if args.json_out:
        payload = {
            "stats": stats,
            "lessons": [asdict(l) | {"completeness": l.completeness_score()} for l in lessons],
        }
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n✅ JSON raporu kaydedildi: {args.json_out}")


if __name__ == "__main__":
    main()


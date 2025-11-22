#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSB Dijital Okuryazarlık Eğitimi - Kurs Takip Sistemi
=====================================================

Bu script, 12 saatlik dijital okuryazarlık eğitiminin ilerlemesini
takip etmek ve raporlamak için kullanılır.

Özellikler:
- Öğrenci katılım takibi
- Ders tamamlama oranları
- Proje submission tracking
- Progress reporting
- Sertifika uygunluk kontrolü

Yazar: Bahattin Yunus Çetin
Tarih: 19 Kasım 2024
Versiyon: 1.0
"""

import csv
import datetime
import json
import os
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional


@dataclass
class Student:
    """Öğrenci bilgi modeli"""

    id: str
    name: str
    email: str
    phone: str
    school: str
    grade: int
    registration_date: str
    attendance: Dict[str, bool] = None
    projects: Dict[str, str] = None  # ders_id: status (completed/pending/not_started)
    total_score: float = 0.0

    def __post_init__(self):
        if self.attendance is None:
            self.attendance = {}
        if self.projects is None:
            self.projects = {}


@dataclass
class Lesson:
    """Ders bilgi modeli"""

    id: str
    title: str
    duration: int  # dakika
    tools: List[str]
    learning_objectives: List[str]
    project_required: bool = True
    min_score: float = 70.0


class CourseTracker:
    """Ana kurs takip sistemi"""

    def __init__(self, data_file: str = "course_data.json"):
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.lessons: Dict[str, Lesson] = {}
        self._initialize_lessons()
        self._load_data()

    def _initialize_lessons(self):
        """12 dersin tanımlarını oluştur"""
        lessons_data = [
            {
                "id": "01",
                "title": "Canva - Dijital Tasarımın Temelleri",
                "duration": 60,
                "tools": ["Canva"],
                "learning_objectives": [
                    "Grafik tasarım",
                    "Poster oluşturma",
                    "Sosyal medya grafiği",
                ],
            },
            {
                "id": "02",
                "title": "Google Dokümanlar - Bulut Tabanlı Yazım",
                "duration": 60,
                "tools": ["Google Docs"],
                "learning_objectives": [
                    "İşbirlikçi yazım",
                    "Bulut depolama",
                    "Belge paylaşımı",
                ],
            },
            {
                "id": "03",
                "title": "Google Slaytlar - Sunum Hazırlama",
                "duration": 60,
                "tools": ["Google Slides"],
                "learning_objectives": ["Etkili sunum", "Görsel tasarım", "Animasyon"],
            },
            {
                "id": "04",
                "title": "Google Formlar - Anket Oluşturma",
                "duration": 60,
                "tools": ["Google Forms"],
                "learning_objectives": ["Anket tasarımı", "Veri toplama", "Analiz"],
            },
            {
                "id": "05",
                "title": "Trello - Dijital Planlama",
                "duration": 60,
                "tools": ["Trello"],
                "learning_objectives": ["Proje yönetimi", "Kanban", "Ekip çalışması"],
            },
            {
                "id": "06",
                "title": "Notion - Bilgi Yönetimi",
                "duration": 60,
                "tools": ["Notion"],
                "learning_objectives": ["Not alma", "Veritabanı", "Organizasyon"],
            },
            {
                "id": "07",
                "title": "Google Drive - Dosya Yönetimi",
                "duration": 60,
                "tools": ["Google Drive"],
                "learning_objectives": ["Bulut depolama", "Paylaşım", "Organizasyon"],
            },
            {
                "id": "08",
                "title": "Siber Güvenlik Temelleri",
                "duration": 60,
                "tools": ["Güvenlik araçları"],
                "learning_objectives": [
                    "Şifre güvenliği",
                    "2FA",
                    "Phishing farkındalığı",
                ],
            },
            {
                "id": "09",
                "title": "Yapay Zeka Temelleri",
                "duration": 60,
                "tools": ["AI araçları"],
                "learning_objectives": [
                    "AI farkındalığı",
                    "Etik kullanım",
                    "Gelecek trendleri",
                ],
            },
            {
                "id": "10",
                "title": "ChatGPT - Doğru Prompt Yazma",
                "duration": 60,
                "tools": ["ChatGPT"],
                "learning_objectives": [
                    "Prompt engineering",
                    "AI iletişimi",
                    "Verimli kullanım",
                ],
            },
            {
                "id": "11",
                "title": "CapCut - Basit Video Düzenleme",
                "duration": 60,
                "tools": ["CapCut"],
                "learning_objectives": [
                    "Video editing",
                    "Sosyal medya içeriği",
                    "Yaratıcılık",
                ],
            },
            {
                "id": "12",
                "title": "Sosyal Medya ve Dijital Etik",
                "duration": 60,
                "tools": ["Çeşitli platformlar"],
                "learning_objectives": [
                    "Dijital vatandaşlık",
                    "Etik kullanım",
                    "Bilgi kirliliği",
                ],
            },
        ]

        for lesson_data in lessons_data:
            lesson = Lesson(**lesson_data)
            self.lessons[lesson.id] = lesson

    def add_student(self, student_data: dict) -> bool:
        """Yeni öğrenci ekle"""
        try:
            # Gerekli alanların kontrolü
            required_fields = ["id", "name", "email", "phone", "school", "grade"]
            for field in required_fields:
                if field not in student_data:
                    raise ValueError(f"Eksik alan: {field}")

            # Tarih ekle
            student_data["registration_date"] = datetime.datetime.now().isoformat()

            student = Student(**student_data)
            self.students[student.id] = student

            # Tüm dersler için başlangıç durumu
            for lesson_id in self.lessons.keys():
                student.attendance[lesson_id] = False
                student.projects[lesson_id] = "not_started"

            print(f"✅ Öğrenci eklendi: {student.name} ({student.id})")
            return True

        except Exception as e:
            print(f"❌ Öğrenci eklenirken hata: {e}")
            return False

    def mark_attendance(
        self, student_id: str, lesson_id: str, present: bool = True
    ) -> bool:
        """Devam durumu güncelle"""
        try:
            if student_id not in self.students:
                raise ValueError(f"Öğrenci bulunamadı: {student_id}")

            if lesson_id not in self.lessons:
                raise ValueError(f"Ders bulunamadı: {lesson_id}")

            self.students[student_id].attendance[lesson_id] = present
            status = "✅ Katıldı" if present else "❌ Katılmadı"
            print(
                f"{status}: {self.students[student_id].name} - {self.lessons[lesson_id].title}"
            )
            return True

        except Exception as e:
            print(f"❌ Devam kaydı hatası: {e}")
            return False

    def update_project_status(
        self, student_id: str, lesson_id: str, status: str
    ) -> bool:
        """Proje durumu güncelle"""
        valid_statuses = ["not_started", "in_progress", "completed", "pending_review"]

        try:
            if student_id not in self.students:
                raise ValueError(f"Öğrenci bulunamadı: {student_id}")

            if lesson_id not in self.lessons:
                raise ValueError(f"Ders bulunamadı: {lesson_id}")

            if status not in valid_statuses:
                raise ValueError(f"Geçersiz durum: {status}")

            self.students[student_id].projects[lesson_id] = status

            status_tr = {
                "not_started": "Başlanmadı",
                "in_progress": "Devam Ediyor",
                "completed": "Tamamlandı",
                "pending_review": "İnceleme Bekliyor",
            }

            print(
                f"📝 Proje durumu: {self.students[student_id].name} - {self.lessons[lesson_id].title}: {status_tr[status]}"
            )
            return True

        except Exception as e:
            print(f"❌ Proje durumu güncellenirken hata: {e}")
            return False

    def calculate_student_progress(self, student_id: str) -> dict:
        """Öğrenci ilerlemesini hesapla"""
        if student_id not in self.students:
            return {}

        student = self.students[student_id]
        total_lessons = len(self.lessons)

        # Katılım oranı
        attended_lessons = sum(
            1 for attended in student.attendance.values() if attended
        )
        attendance_rate = (attended_lessons / total_lessons) * 100

        # Proje tamamlama oranı
        completed_projects = sum(
            1 for status in student.projects.values() if status == "completed"
        )
        project_completion_rate = (completed_projects / total_lessons) * 100

        # Genel ilerleme
        overall_progress = (attendance_rate + project_completion_rate) / 2

        # Sertifika uygunluğu
        certificate_eligible = attendance_rate >= 80 and project_completion_rate >= 70

        return {
            "student_name": student.name,
            "attendance_rate": round(attendance_rate, 1),
            "project_completion_rate": round(project_completion_rate, 1),
            "overall_progress": round(overall_progress, 1),
            "attended_lessons": attended_lessons,
            "completed_projects": completed_projects,
            "total_lessons": total_lessons,
            "certificate_eligible": certificate_eligible,
        }

    def generate_class_report(self) -> dict:
        """Sınıf genel raporu oluştur"""
        if not self.students:
            return {"error": "Kayıtlı öğrenci yok"}

        total_students = len(self.students)
        progress_data = []

        for student_id in self.students.keys():
            progress = self.calculate_student_progress(student_id)
            progress_data.append(progress)

        # Ortalama hesaplamaları
        avg_attendance = (
            sum(p["attendance_rate"] for p in progress_data) / total_students
        )
        avg_project_completion = (
            sum(p["project_completion_rate"] for p in progress_data) / total_students
        )
        avg_overall_progress = (
            sum(p["overall_progress"] for p in progress_data) / total_students
        )

        certificate_eligible_count = sum(
            1 for p in progress_data if p["certificate_eligible"]
        )
        certificate_rate = (certificate_eligible_count / total_students) * 100

        # Ders bazında katılım
        lesson_attendance = {}
        for lesson_id, lesson in self.lessons.items():
            attended = sum(
                1
                for student in self.students.values()
                if student.attendance.get(lesson_id, False)
            )
            lesson_attendance[lesson.title] = {
                "attended": attended,
                "total": total_students,
                "rate": round((attended / total_students) * 100, 1),
            }

        return {
            "report_date": datetime.datetime.now().isoformat(),
            "total_students": total_students,
            "averages": {
                "attendance_rate": round(avg_attendance, 1),
                "project_completion_rate": round(avg_project_completion, 1),
                "overall_progress": round(avg_overall_progress, 1),
            },
            "certificate_eligibility": {
                "eligible_students": certificate_eligible_count,
                "eligibility_rate": round(certificate_rate, 1),
            },
            "lesson_attendance": lesson_attendance,
            "student_details": progress_data,
        }

    def export_to_csv(self, filename: str = None) -> bool:
        """CSV formatında dışa aktar"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gsb_kurs_raporu_{timestamp}.csv"

        try:
            with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
                fieldnames = [
                    "Öğrenci ID",
                    "İsim",
                    "E-posta",
                    "Okul",
                    "Sınıf",
                    "Kayıt Tarihi",
                    "Katılım Oranı (%)",
                    "Proje Tamamlama (%)",
                    "Genel İlerleme (%)",
                    "Sertifika Uygun",
                ]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for student_id, student in self.students.items():
                    progress = self.calculate_student_progress(student_id)
                    writer.writerow(
                        {
                            "Öğrenci ID": student.id,
                            "İsim": student.name,
                            "E-posta": student.email,
                            "Okul": student.school,
                            "Sınıf": student.grade,
                            "Kayıt Tarihi": student.registration_date.split("T")[0],
                            "Katılım Oranı (%)": progress["attendance_rate"],
                            "Proje Tamamlama (%)": progress["project_completion_rate"],
                            "Genel İlerleme (%)": progress["overall_progress"],
                            "Sertifika Uygun": "Evet"
                            if progress["certificate_eligible"]
                            else "Hayır",
                        }
                    )

            print(f"✅ CSV raporu oluşturuldu: {filename}")
            return True

        except Exception as e:
            print(f"❌ CSV dışa aktarım hatası: {e}")
            return False

    def _load_data(self):
        """Kayıtlı veriyi yükle"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                for student_data in data.get("students", []):
                    student = Student(**student_data)
                    self.students[student.id] = student

                print(f"✅ {len(self.students)} öğrenci verisi yüklendi")
        except Exception as e:
            print(f"⚠️ Veri yükleme hatası: {e}")

    def save_data(self):
        """Veriyi kaydet"""
        try:
            data = {
                "students": [asdict(student) for student in self.students.values()],
                "last_updated": datetime.datetime.now().isoformat(),
            }

            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✅ Veri kaydedildi: {self.data_file}")
            return True

        except Exception as e:
            print(f"❌ Veri kaydetme hatası: {e}")
            return False


def main():
    """Ana fonksiyon - Demo kullanım"""
    print("🚀 GSB Dijital Okuryazarlık Eğitimi - Kurs Takip Sistemi")
    print("=" * 60)

    # Tracker'ı başlat
    tracker = CourseTracker()

    # Demo öğrenciler ekle
    sample_students = [
        {
            "id": "GSB001",
            "name": "Ahmet Yılmaz",
            "email": "ahmet@email.com",
            "phone": "0555-123-4567",
            "school": "Atatürk Lisesi",
            "grade": 11,
        },
        {
            "id": "GSB002",
            "name": "Ayşe Kaya",
            "email": "ayse@email.com",
            "phone": "0555-234-5678",
            "school": "Cumhuriyet Lisesi",
            "grade": 10,
        },
        {
            "id": "GSB003",
            "name": "Mehmet Demir",
            "email": "mehmet@email.com",
            "phone": "0555-345-6789",
            "school": "Gazi Lisesi",
            "grade": 12,
        },
    ]

    # Öğrencileri ekle
    for student_data in sample_students:
        tracker.add_student(student_data)

    print("\n📊 Demo Veri Girişi...")

    # Demo katılım ve proje verileri
    demo_data = [
        ("GSB001", "01", True, "completed"),
        ("GSB001", "02", True, "completed"),
        ("GSB001", "03", True, "in_progress"),
        ("GSB002", "01", True, "completed"),
        ("GSB002", "02", False, "not_started"),
        ("GSB003", "01", True, "pending_review"),
    ]

    for student_id, lesson_id, attendance, project_status in demo_data:
        tracker.mark_attendance(student_id, lesson_id, attendance)
        tracker.update_project_status(student_id, lesson_id, project_status)

    print("\n📈 Bireysel İlerleme Raporları:")
    print("-" * 40)

    for student_id in tracker.students.keys():
        progress = tracker.calculate_student_progress(student_id)
        print(f"👤 {progress['student_name']}")
        print(f"   📅 Katılım: %{progress['attendance_rate']}")
        print(f"   📝 Proje: %{progress['project_completion_rate']}")
        print(f"   📊 Genel: %{progress['overall_progress']}")
        print(
            f"   🎓 Sertifika: {'✅ Uygun' if progress['certificate_eligible'] else '❌ Uygun Değil'}"
        )
        print()

    print("\n📊 Sınıf Genel Raporu:")
    print("-" * 40)

    class_report = tracker.generate_class_report()
    print(f"👥 Toplam Öğrenci: {class_report['total_students']}")
    print(f"📅 Ortalama Katılım: %{class_report['averages']['attendance_rate']}")
    print(
        f"📝 Ortalama Proje Tamamlama: %{class_report['averages']['project_completion_rate']}"
    )
    print(
        f"🎓 Sertifika Uygun: {class_report['certificate_eligibility']['eligible_students']}/{class_report['total_students']} (%{class_report['certificate_eligibility']['eligibility_rate']})"
    )

    print("\n💾 Veri Kaydetme ve Dışa Aktarma...")
    tracker.save_data()
    tracker.export_to_csv()

    print("\n🎉 Demo tamamlandı! Dosyalar oluşturuldu.")
    print("📁 course_data.json - Ana veri dosyası")
    print("📊 gsb_kurs_raporu_*.csv - Excel raporu")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSB Dijital Okuryazarlık Eğitimi - Yardımcı Fonksiyonlar
======================================================

Bu modül, eğitim sürecinde kullanılan ortak yardımcı fonksiyonları
ve utility class'larını içerir.

Özellikler:
- Dosya işlemleri
- Veri validasyonu
- Rapor oluşturma
- Email gönderimi
- Excel/CSV işlemleri
- Markdown işleme

Yazar: Bahattin Yunus Çetin
Tarih: 19 Kasım 2024
Versiyon: 1.0
"""

import csv
import datetime
import hashlib
import json
import logging
import os
import re
import smtplib
import urllib.parse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("gsb_education.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class FileManager:
    """Dosya işlemleri için yardımcı sınıf"""

    @staticmethod
    def create_directory(path: str, parents: bool = True) -> bool:
        """Dizin oluşturma"""
        try:
            Path(path).mkdir(parents=parents, exist_ok=True)
            logger.info(f"Dizin oluşturuldu: {path}")
            return True
        except Exception as e:
            logger.error(f"Dizin oluşturma hatası: {e}")
            return False

    @staticmethod
    def read_file(file_path: str, encoding: str = "utf-8") -> Optional[str]:
        """Dosya okuma"""
        try:
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read()
            logger.info(f"Dosya okundu: {file_path}")
            return content
        except Exception as e:
            logger.error(f"Dosya okuma hatası: {e}")
            return None

    @staticmethod
    def write_file(file_path: str, content: str, encoding: str = "utf-8") -> bool:
        """Dosya yazma"""
        try:
            # Dizin yoksa oluştur
            FileManager.create_directory(os.path.dirname(file_path))

            with open(file_path, "w", encoding=encoding) as f:
                f.write(content)
            logger.info(f"Dosya yazıldı: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Dosya yazma hatası: {e}")
            return False

    @staticmethod
    def copy_file(source: str, destination: str) -> bool:
        """Dosya kopyalama"""
        try:
            import shutil

            shutil.copy2(source, destination)
            logger.info(f"Dosya kopyalandı: {source} -> {destination}")
            return True
        except Exception as e:
            logger.error(f"Dosya kopyalama hatası: {e}")
            return False

    @staticmethod
    def get_file_hash(file_path: str) -> Optional[str]:
        """Dosya hash'i hesaplama"""
        try:
            with open(file_path, "rb") as f:
                content = f.read()
                hash_value = hashlib.md5(content).hexdigest()
            return hash_value
        except Exception as e:
            logger.error(f"Hash hesaplama hatası: {e}")
            return None

    @staticmethod
    def list_files(directory: str, extension: str = None) -> List[str]:
        """Dizindeki dosyaları listeleme"""
        try:
            files = []
            for file_path in Path(directory).rglob("*"):
                if file_path.is_file():
                    if (
                        extension is None
                        or file_path.suffix.lower() == extension.lower()
                    ):
                        files.append(str(file_path))
            return sorted(files)
        except Exception as e:
            logger.error(f"Dosya listeleme hatası: {e}")
            return []


class DataValidator:
    """Veri doğrulama fonksiyonları"""

    @staticmethod
    def validate_email(email: str) -> bool:
        """E-posta formatı kontrolü"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Telefon numarası formatı kontrolü"""
        # Türkiye telefon format: 05xx-xxx-xxxx veya 0xxx-xxx-xxxx
        phone = re.sub(r"[^\d]", "", phone)
        return bool(re.match(r"^0[5-9]\d{9}$", phone))

    @staticmethod
    def validate_student_id(student_id: str) -> bool:
        """Öğrenci ID formatı kontrolü"""
        # GSB001, GSB002 formatında
        pattern = r"^GSB\d{3}$"
        return bool(re.match(pattern, student_id))

    @staticmethod
    def validate_lesson_id(lesson_id: str) -> bool:
        """Ders ID formatı kontrolü"""
        # 01, 02, ... 12 formatında
        return lesson_id in [f"{i:02d}" for i in range(1, 13)]

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Dosya adını güvenli hale getirme"""
        # Türkçe karakterleri değiştir
        tr_chars = {
            "ı": "i",
            "ğ": "g",
            "ü": "u",
            "ş": "s",
            "ö": "o",
            "ç": "c",
            "İ": "I",
            "Ğ": "G",
            "Ü": "U",
            "Ş": "S",
            "Ö": "O",
            "Ç": "C",
        }

        for tr_char, en_char in tr_chars.items():
            filename = filename.replace(tr_char, en_char)

        # Güvenli olmayan karakterleri temizle
        filename = re.sub(r'[<>:"/\\|?*]', "_", filename)
        filename = re.sub(r"\s+", "_", filename)
        filename = filename.strip("._")

        return filename


class ExcelExporter:
    """Excel/CSV export işlemleri"""

    @staticmethod
    def export_student_data(students: Dict, filename: str = None) -> str:
        """Öğrenci verilerini CSV'ye aktar"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ogrenci_raporu_{timestamp}.csv"

        try:
            with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
                fieldnames = [
                    "Öğrenci ID",
                    "İsim",
                    "E-posta",
                    "Telefon",
                    "Okul",
                    "Sınıf",
                    "Kayıt Tarihi",
                    "Son Aktivite",
                    "Toplam Katılım",
                    "Proje Sayısı",
                ]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for student_id, student in students.items():
                    attended_count = sum(1 for x in student.attendance.values() if x)
                    completed_projects = sum(
                        1 for x in student.projects.values() if x == "completed"
                    )

                    writer.writerow(
                        {
                            "Öğrenci ID": student.id,
                            "İsim": student.name,
                            "E-posta": student.email,
                            "Telefon": student.phone,
                            "Okul": student.school,
                            "Sınıf": student.grade,
                            "Kayıt Tarihi": student.registration_date.split("T")[0],
                            "Son Aktivite": datetime.datetime.now().strftime(
                                "%Y-%m-%d"
                            ),
                            "Toplam Katılım": attended_count,
                            "Proje Sayısı": completed_projects,
                        }
                    )

            logger.info(f"Excel raporu oluşturuldu: {filename}")
            return filename

        except Exception as e:
            logger.error(f"Excel export hatası: {e}")
            return ""

    @staticmethod
    def export_lesson_statistics(
        lessons: Dict, attendance_data: Dict, filename: str = None
    ) -> str:
        """Ders istatistiklerini CSV'ye aktar"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ders_istatistikleri_{timestamp}.csv"

        try:
            with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
                fieldnames = [
                    "Ders No",
                    "Ders Adı",
                    "Araç",
                    "Toplam Katılım",
                    "Katılım Oranı (%)",
                    "Ortalama Puan",
                    "Tamamlanan Proje",
                ]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for lesson_id, lesson in lessons.items():
                    # İstatistikleri hesapla (örnek veri)
                    total_students = len(attendance_data)
                    attended = sum(
                        1
                        for student_data in attendance_data.values()
                        if student_data.get("attendance", {}).get(lesson_id, False)
                    )
                    attendance_rate = (
                        (attended / total_students * 100) if total_students > 0 else 0
                    )

                    writer.writerow(
                        {
                            "Ders No": lesson_id,
                            "Ders Adı": lesson.title,
                            "Araç": ", ".join(lesson.tools),
                            "Toplam Katılım": attended,
                            "Katılım Oranı (%)": round(attendance_rate, 1),
                            "Ortalama Puan": 85.5,  # Örnek değer
                            "Tamamlanan Proje": attended - 2,  # Örnek hesaplama
                        }
                    )

            logger.info(f"Ders istatistikleri raporu oluşturuldu: {filename}")
            return filename

        except Exception as e:
            logger.error(f"İstatistik export hatası: {e}")
            return ""


class MarkdownProcessor:
    """Markdown işleme fonksiyonları"""

    @staticmethod
    def extract_headings(markdown_content: str) -> List[Dict[str, str]]:
        """Markdown'dan başlıkları çıkart"""
        headings = []
        lines = markdown_content.split("\n")

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if line.startswith("#"):
                level = len(line) - len(line.lstrip("#"))
                title = line.lstrip("# ").strip()
                headings.append({"level": level, "title": title, "line": line_num})

        return headings

    @staticmethod
    def create_table_of_contents(markdown_content: str) -> str:
        """İçindekiler tablosu oluştur"""
        headings = MarkdownProcessor.extract_headings(markdown_content)
        toc = ["## İçindekiler\n"]

        for heading in headings:
            if heading["level"] <= 3:  # Sadece H1, H2, H3
                indent = "  " * (heading["level"] - 1)
                # Başlığı URL-safe anchor'a çevir
                anchor = heading["title"].lower()
                anchor = re.sub(r"[^\w\s-]", "", anchor)
                anchor = re.sub(r"[-\s]+", "-", anchor)

                toc.append(f"{indent}- [{heading['title']}](#{anchor})")

        return "\n".join(toc) + "\n"

    @staticmethod
    def validate_links(markdown_content: str) -> List[Dict[str, Any]]:
        """Markdown linklerini doğrula"""
        link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        links = re.findall(link_pattern, markdown_content)

        link_status = []
        for text, url in links:
            status = {"text": text, "url": url, "valid": True, "type": "unknown"}

            if url.startswith("http"):
                status["type"] = "external"
                # URL doğrulama (basit kontrol)
                try:
                    parsed = urllib.parse.urlparse(url)
                    status["valid"] = bool(parsed.netloc)
                except:
                    status["valid"] = False
            elif url.startswith("#"):
                status["type"] = "anchor"
            elif url.startswith("./") or url.startswith("../"):
                status["type"] = "relative"
                # Dosya varlığı kontrolü yapılabilir
            else:
                status["type"] = "absolute"

            link_status.append(status)

        return link_status


class EmailNotification:
    """E-posta bildirimleri"""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_completion_certificate(
        self, student_email: str, student_name: str, completion_rate: float
    ) -> bool:
        """Tamamlama sertifikası e-postası gönder"""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.username
            msg["To"] = student_email
            msg["Subject"] = (
                "🎓 GSB Dijital Okuryazarlık Eğitimi - Tamamlama Sertifikanız"
            )

            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; color: white;">
                    <h1>🎉 Tebrikler {student_name}!</h1>
                    <p style="font-size: 18px;">GSB Dijital Okuryazarlık Eğitimini başarıyla tamamladınız!</p>
                </div>

                <div style="padding: 30px; background: #f8f9fa;">
                    <h2 style="color: #333;">📊 Başarı Özeti</h2>
                    <ul style="font-size: 16px; line-height: 1.6;">
                        <li><strong>Tamamlama Oranı:</strong> %{completion_rate:.1f}</li>
                        <li><strong>Öğrenilen Araçlar:</strong> 8+ dijital platform</li>
                        <li><strong>Tamamlanan Projeler:</strong> 20+ pratik çalışma</li>
                        <li><strong>Toplam Eğitim Süresi:</strong> 12 saat</li>
                    </ul>

                    <h3 style="color: #333;">🛠️ Kazandığınız Yetenekler</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div>✅ Canva ile Tasarım</div>
                        <div>✅ Google Workspace</div>
                        <div>✅ Proje Yönetimi</div>
                        <div>✅ AI Araçları Kullanımı</div>
                        <div>✅ Video Düzenleme</div>
                        <div>✅ Dijital Güvenlik</div>
                    </div>
                </div>

                <div style="padding: 20px; text-align: center; background: #667eea; color: white;">
                    <p>Bu sertifika, Gençlik ve Spor Bakanlığı tarafından onaylanmıştır.</p>
                    <p><strong>Dijital geleceğiniz başlıyor! 🚀</strong></p>
                </div>
            </body>
            </html>
            """

            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            logger.info(f"Sertifika e-postası gönderildi: {student_email}")
            return True

        except Exception as e:
            logger.error(f"E-posta gönderme hatası: {e}")
            return False

    def send_progress_report(self, instructor_email: str, class_report: Dict) -> bool:
        """Eğitmene ilerleme raporu gönder"""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.username
            msg["To"] = instructor_email
            msg["Subject"] = "📊 GSB Eğitimi - Haftalık İlerleme Raporu"

            # Rapor içeriğini hazırla
            total_students = class_report.get("total_students", 0)
            avg_attendance = class_report.get("averages", {}).get("attendance_rate", 0)
            eligible_count = class_report.get("certificate_eligibility", {}).get(
                "eligible_students", 0
            )

            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif;">
                <h2>📊 GSB Dijital Okuryazarlık Eğitimi - İlerleme Raporu</h2>

                <h3>📈 Genel İstatistikler</h3>
                <ul>
                    <li><strong>Toplam Öğrenci:</strong> {total_students}</li>
                    <li><strong>Ortalama Katılım:</strong> %{avg_attendance:.1f}</li>
                    <li><strong>Sertifika Almaya Uygun:</strong> {eligible_count} öğrenci</li>
                </ul>

                <h3>📚 Ders Bazında Katılım</h3>
                <table border="1" style="border-collapse: collapse; width: 100%;">
                    <tr style="background: #f0f0f0;">
                        <th>Ders</th>
                        <th>Katılan</th>
                        <th>Oran</th>
                    </tr>
            """

            for lesson, data in class_report.get("lesson_attendance", {}).items():
                html_body += f"""
                    <tr>
                        <td>{lesson}</td>
                        <td>{data["attended"]}/{data["total"]}</td>
                        <td>%{data["rate"]}</td>
                    </tr>
                """

            html_body += (
                """
                </table>

                <p><strong>Rapor Tarihi:</strong> """
                + datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
                + """</p>

                <hr>
                <p style="color: #666; font-size: 12px;">
                Bu rapor otomatik olarak oluşturulmuştur.
                Detaylı bilgi için GSB Eğitim Platformunu ziyaret edin.
                </p>
            </body>
            </html>
            """
            )

            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            logger.info(f"İlerleme raporu gönderildi: {instructor_email}")
            return True

        except Exception as e:
            logger.error(f"Rapor e-postası hatası: {e}")
            return False


class ConfigManager:
    """Konfigürasyon yönetimi"""

    DEFAULT_CONFIG = {
        "course": {
            "name": "GSB Dijital Okuryazarlık Eğitimi",
            "duration_hours": 12,
            "total_lessons": 12,
            "min_attendance_rate": 80.0,
            "min_project_completion_rate": 70.0,
        },
        "notifications": {
            "send_completion_emails": True,
            "send_progress_reports": True,
            "report_frequency_days": 7,
        },
        "file_settings": {
            "backup_enabled": True,
            "backup_frequency_hours": 24,
            "max_backup_files": 10,
        },
        "security": {
            "password_min_length": 8,
            "session_timeout_minutes": 60,
            "max_login_attempts": 3,
        },
    }

    def __init__(self, config_file: str = "gsb_config.json"):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Konfigürasyonu yükle"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                # Default değerlerle birleştir
                return self._merge_config(self.DEFAULT_CONFIG, config)
            else:
                # Default config'i kaydet
                self.save_config(self.DEFAULT_CONFIG)
                return self.DEFAULT_CONFIG.copy()
        except Exception as e:
            logger.error(f"Config yükleme hatası: {e}")
            return self.DEFAULT_CONFIG.copy()

    def _merge_config(self, default: Dict, loaded: Dict) -> Dict:
        """İki config'i birleştir"""
        merged = default.copy()
        for key, value in loaded.items():
            if (
                key in merged
                and isinstance(merged[key], dict)
                and isinstance(value, dict)
            ):
                merged[key] = self._merge_config(merged[key], value)
            else:
                merged[key] = value
        return merged

    def save_config(self, config: Dict = None) -> bool:
        """Konfigürasyonu kaydet"""
        try:
            config_to_save = config or self.config
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config_to_save, f, ensure_ascii=False, indent=2)
            logger.info(f"Config kaydedildi: {self.config_file}")
            return True
        except Exception as e:
            logger.error(f"Config kaydetme hatası: {e}")
            return False

    def get(self, key_path: str, default=None):
        """Nested key ile değer al (örnek: 'course.duration_hours')"""
        keys = key_path.split(".")
        value = self.config

        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        return value

    def set(self, key_path: str, value) -> bool:
        """Nested key ile değer ata"""
        keys = key_path.split(".")
        config = self.config

        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]

        config[keys[-1]] = value
        return self.save_config()


# Utility fonksiyonları
def format_turkish_date(date_obj: datetime.datetime) -> str:
    """Türkçe tarih formatı"""
    months = [
        "Ocak",
        "Şubat",
        "Mart",
        "Nisan",
        "Mayıs",
        "Haziran",
        "Temmuz",
        "Ağustos",
        "Eylül",
        "Ekim",
        "Kasım",
        "Aralık",
    ]

    days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

    day_name = days[date_obj.weekday()]
    month_name = months[date_obj.month - 1]

    return f"{day_name}, {date_obj.day} {month_name} {date_obj.year}"


def generate_student_id() -> str:
    """Otomatik öğrenci ID üretimi"""
    timestamp = datetime.datetime.now().strftime("%m%d%H%M")
    return f"GSB{timestamp[-3:]}"


def calculate_progress_percentage(completed: int, total: int) -> float:
    """İlerleme yüzdesi hesaplama"""
    if total == 0:
        return 0.0
    return round((completed / total) * 100, 1)


def time_until_deadline(deadline: datetime.datetime) -> str:
    """Deadline'a kalan süreyi hesapla"""
    now = datetime.datetime.now()
    diff = deadline - now

    if diff.total_seconds() < 0:
        return "Süresi doldu"

    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    if days > 0:
        return f"{days} gün {hours} saat"
    elif hours > 0:
        return f"{hours} saat {minutes} dakika"
    else:
        return f"{minutes} dakika"


# Demo fonksiyon
def main():
    """Utility fonksiyonların demo kullanımı"""
    print("🛠️ GSB Eğitimi - Utility Fonksiyonlar Demo")
    print("=" * 50)

    # Dosya işlemleri
    print("\n📁 Dosya İşlemleri:")
    FileManager.create_directory("test_data")
    FileManager.write_file("test_data/demo.txt", "Test içeriği")
    content = FileManager.read_file("test_data/demo.txt")
    print(f"Okunan içerik: {content}")

    # Veri doğrulama
    print("\n✅ Veri Doğrulama:")
    test_emails = ["test@example.com", "invalid-email", "user@domain.co.uk"]
    for email in test_emails:
        is_valid = DataValidator.validate_email(email)
        print(f"{email}: {'✅ Geçerli' if is_valid else '❌ Geçersiz'}")

    # Tarih formatı
    print(f"\n📅 Türkçe Tarih: {format_turkish_date(datetime.datetime.now())}")

    # ID üretimi
    print(f"🆔 Otomatik ID: {generate_student_id()}")

    # Progress hesaplama
    progress = calculate_progress_percentage(8, 12)
    print(f"📊 İlerleme: %{progress}")

    # Config yönetimi
    print("\n⚙️ Config Test:")
    config = ConfigManager()
    print(f"Kurs adı: {config.get('course.name')}")
    print(f"Minimum katılım: {config.get('course.min_attendance_rate')}")

    print("\n🎉 Demo tamamlandı!")


if __name__ == "__main__":
    main()

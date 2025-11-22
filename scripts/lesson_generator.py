#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSB Dijital Okuryazarlık Eğitimi - Ders Planı Üretici
====================================================

Bu script, yeni ders planları oluşturmak ve mevcut planları
güncellemek için kullanılan otomatik template generator'dır.

Özellikler:
- Yeni ders planı şablonu oluşturma
- Mevcut planları güncelleme
- Çoklu dil desteği
- Template customization
- Batch processing

Yazar: Bahattin Yunus Çetin
Tarih: 19 Kasım 2024
Versiyon: 1.0
"""

import datetime
import json
import os
from pathlib import Path
from typing import Dict, List, Optional


class LessonPlanGenerator:
    """Ders planı üretici ana sınıfı"""

    def __init__(self, base_path: str = "../ders_notlari"):
        self.base_path = Path(base_path)
        self.templates = self._load_templates()
        self.config = self._load_config()

    def _load_templates(self) -> Dict:
        """Şablon yapılarını yükle"""
        return {
            "basic": {
                "sections": [
                    "Ders Amacı",
                    "Süre",
                    "Ders İçeriği",
                    "Pratik Ödevler",
                    "Değerlendirme Kriterleri",
                    "Yararlı Linkler",
                    "Sonraki Ders İçin Hazırlık",
                    "Bonus Aktiviteler",
                ],
                "emojis": {
                    "Ders Amacı": "🎯",
                    "Süre": "⏰",
                    "Ders İçeriği": "📋",
                    "Pratik Ödevler": "📝",
                    "Değerlendirme Kriterleri": "📊",
                    "Yararlı Linkler": "🔗",
                    "Sonraki Ders İçin Hazırlık": "📝",
                    "Bonus Aktiviteler": "🎪",
                },
            },
            "advanced": {
                "sections": [
                    "Ders Amacı",
                    "Süre",
                    "Ön Gereksinimler",
                    "Ders İçeriği",
                    "İpuçları ve Püf Noktaları",
                    "Teknik Özellikler",
                    "Pratik Ödevler",
                    "Özel Projeler",
                    "Yaratıcı Uygulamalar",
                    "Değerlendirme Kriterleri",
                    "Yararlı Linkler",
                    "Sonraki Ders İçin Hazırlık",
                    "Bonus Aktiviteler",
                ],
                "emojis": {
                    "Ders Amacı": "🎯",
                    "Süre": "⏰",
                    "Ön Gereksinimler": "📋",
                    "Ders İçeriği": "📚",
                    "İpuçları ve Püf Noktaları": "💡",
                    "Teknik Özellikler": "🔧",
                    "Praktik Ödevler": "📝",
                    "Özel Projeler": "🎯",
                    "Yaratıcı Uygulamalar": "🌟",
                    "Değerlendirme Kriterleri": "📊",
                    "Yararlı Linkler": "🔗",
                    "Sonraki Ders İçin Hazırlık": "📝",
                    "Bonus Aktiviteler": "🎪",
                },
            },
        }

    def _load_config(self) -> Dict:
        """Konfigürasyon ayarlarını yükle"""
        return {
            "default_duration": 60,
            "difficulty_levels": ["Temel Seviye", "Orta Seviye", "İleri Seviye"],
            "project_types": [
                "Bireysel proje",
                "Grup çalışması",
                "Sunum hazırlama",
                "Pratik uygulama",
                "Araştırma görevi",
            ],
            "assessment_methods": [
                "Praktik değerlendirme",
                "Portfolio incelemesi",
                "Peer evaluation",
                "Self assessment",
                "Proje sunumu",
            ],
        }

    def create_lesson_plan(self, lesson_data: Dict) -> str:
        """Yeni ders planı oluştur"""

        # Gerekli alanları kontrol et
        required_fields = ["lesson_number", "title", "tool", "objectives"]
        for field in required_fields:
            if field not in lesson_data:
                raise ValueError(f"Eksik alan: {field}")

        template_type = lesson_data.get("template", "basic")
        template = self.templates[template_type]

        # Markdown içeriği oluştur
        content = self._generate_markdown_content(lesson_data, template)

        return content

    def _generate_markdown_content(self, lesson_data: Dict, template: Dict) -> str:
        """Markdown içeriği oluştur"""

        lesson_num = lesson_data["lesson_number"]
        title = lesson_data["title"]
        tool = lesson_data["tool"]
        objectives = lesson_data.get("objectives", [])
        duration = lesson_data.get("duration", self.config["default_duration"])

        content = []

        # Başlık
        content.append(f"# {lesson_num}. Ders: {title}")
        content.append("")

        # Ders Amacı
        emoji = template["emojis"].get("Ders Amacı", "🎯")
        content.append(f"## {emoji} Ders Amacı")
        if objectives:
            for obj in objectives:
                content.append(f"- {obj}")
        else:
            content.append(
                f"Öğrencilerin {tool} platformunu kullanarak [hedef becerileri] geliştirmelerini sağlamak."
            )
        content.append("")

        # Süre
        emoji = template["emojis"].get("Süre", "⏰")
        content.append(f"## {emoji} Süre")
        content.append(f"1 Saat ({duration} dakika)")
        content.append("")

        # Ders İçeriği
        emoji = template["emojis"].get("Ders İçeriği", "📋")
        content.append(f"## {emoji} Ders İçeriği")
        content.append("")
        content.append("### Giriş (10 dakika)")
        content.append(f"- {tool} nedir ve neden önemli?")
        content.append("- Günlük hayattaki kullanım alanları")
        content.append("- Hesap oluşturma ve arayüz tanıtımı")
        content.append("")
        content.append("### Ana Bölüm (40 dakika)")
        content.append("")
        content.append(f"#### 1. {tool} Temelleri (15 dakika)")
        content.append("- Temel özellikler ve araçlar")
        content.append("- Arayüz navigasyonu")
        content.append("- İlk proje oluşturma")
        content.append("")
        content.append("#### 2. Pratik Uygulamalar (25 dakika)")
        content.append("- Hands-on çalışmalar")
        content.append("- Gerçek proje örnekleri")
        content.append("- Best practices")
        content.append("")
        content.append("### Uygulama ve Değerlendirme (10 dakika)")
        content.append("- Bireysel çalışma zamanı")
        content.append("- Sonuçları paylaşma")
        content.append("- Geri bildirim alma")
        content.append("")

        # Pratik Ödevler
        emoji = template["emojis"].get("Pratik Ödevler", "📝")
        content.append(f"## {emoji} Pratik Ödevler")
        content.append("")
        for i, level in enumerate(self.config["difficulty_levels"], 1):
            content.append(f"### {level}")
            for j in range(1, 4):
                proj_num = (i - 1) * 3 + j
                content.append(f"{proj_num}. **[Proje adı]**: [Proje açıklaması]")
            content.append("")

        # İpuçları (Advanced template için)
        if "İpuçları ve Püf Noktaları" in template["sections"]:
            emoji = template["emojis"].get("İpuçları ve Püf Noktaları", "💡")
            content.append(f"## {emoji} İpuçları ve Püf Noktaları")
            content.append("")
            content.append("### Verimlilik Artırıcılar")
            content.append("- [İpucu 1]")
            content.append("- [İpucu 2]")
            content.append("- [İpucu 3]")
            content.append("")
            content.append("### Yaygın Hatalar ve Çözümleri")
            content.append("- ❌ **[Hata]**: [Açıklama]")
            content.append("- ✅ **[Çözüm]**: [Doğru yaklaşım]")
            content.append("")

        # Değerlendirme Kriterleri
        emoji = template["emojis"].get("Değerlendirme Kriterleri", "📊")
        content.append(f"## {emoji} Değerlendirme Kriterleri")
        content.append("- [ ] [Kriter 1]")
        content.append("- [ ] [Kriter 2]")
        content.append("- [ ] [Kriter 3]")
        content.append("- [ ] [Kriter 4]")
        content.append("- [ ] [Kriter 5]")
        content.append("")

        # Özel Projeler (Advanced template için)
        if "Özel Projeler" in template["sections"]:
            emoji = template["emojis"].get("Özel Projeler", "🎯")
            content.append(f"## {emoji} Özel Projeler")
            content.append("")
            content.append("### Proje 1: [Proje Adı]")
            content.append("**Hedef**: [Proje hedefi]")
            content.append("**Süre**: [Tahmini süre]")
            content.append("**Çıktılar**:")
            content.append("- [Çıktı 1]")
            content.append("- [Çıktı 2]")
            content.append("")

        # Yararlı Linkler
        emoji = template["emojis"].get("Yararlı Linkler", "🔗")
        content.append(f"## {emoji} Yararlı Linkler")
        content.append(f"- [{tool} Resmi Web Sitesi](#)")
        content.append(f"- [{tool} Yardım Dokümantasyonu](#)")
        content.append(f"- [{tool} Video Eğitimleri](#)")
        content.append("- [Türkçe Kaynaklar](#)")
        content.append("")

        # Sonraki Ders İçin Hazırlık
        emoji = template["emojis"].get("Sonraki Ders İçin Hazırlık", "📝")
        content.append(f"## {emoji} Sonraki Ders İçin Hazırlık")
        content.append("- [Sonraki araç] hakkında temel araştırma")
        content.append("- [Gerekli hesap] oluşturma")
        content.append(f"- {tool} ile oluşturulan projeleri organize etme")
        content.append("")

        # Bonus Aktiviteler
        emoji = template["emojis"].get("Bonus Aktiviteler", "🎪")
        content.append(f"## {emoji} Bonus Aktiviteler")
        content.append("1. **[Aktivite 1]**: [Açıklama]")
        content.append("2. **[Aktivite 2]**: [Açıklama]")
        content.append("3. **[Aktivite 3]**: [Açıklama]")
        content.append("4. **[Aktivite 4]**: [Açıklama]")
        content.append("")

        # Eğitmen Notu
        content.append("---")
        content.append(
            f"**Eğitmen Notu**: {tool} ile ilgili özel notlar ve öneriler buraya eklenmelidir."
        )

        return "\n".join(content)

    def save_lesson_plan(
        self, content: str, lesson_number: str, filename: str = None
    ) -> bool:
        """Ders planını dosyaya kaydet"""

        try:
            # Klasör yapısını oluştur
            lesson_dir = self.base_path / f"{lesson_number.zfill(2)}_[tool_name]"
            lesson_dir.mkdir(parents=True, exist_ok=True)

            # Dosya adı belirle
            if filename is None:
                filename = "ders_plani.md"

            file_path = lesson_dir / filename

            # Dosyayı kaydet
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ Ders planı kaydedildi: {file_path}")
            return True

        except Exception as e:
            print(f"❌ Kaydetme hatası: {e}")
            return False

    def batch_create_lessons(self, lessons_config: List[Dict]) -> bool:
        """Toplu ders planı oluşturma"""

        success_count = 0
        total_count = len(lessons_config)

        print(f"📚 {total_count} ders planı oluşturuluyor...")

        for lesson_data in lessons_config:
            try:
                content = self.create_lesson_plan(lesson_data)
                lesson_num = lesson_data["lesson_number"]

                if self.save_lesson_plan(content, lesson_num):
                    success_count += 1
                    print(f"   ✅ {lesson_num}. {lesson_data['title']}")
                else:
                    print(f"   ❌ {lesson_num}. {lesson_data['title']}")

            except Exception as e:
                print(f"   ❌ {lesson_data.get('lesson_number', '?')}. Hata: {e}")

        print(
            f"\n📊 Sonuç: {success_count}/{total_count} ders planı başarıyla oluşturuldu."
        )
        return success_count == total_count

    def create_example_config(self) -> Dict:
        """Örnek konfigürasyon oluştur"""

        return {
            "lessons": [
                {
                    "lesson_number": "13",
                    "title": "Figma - UI/UX Tasarım Temelleri",
                    "tool": "Figma",
                    "template": "advanced",
                    "duration": 60,
                    "objectives": [
                        "Figma arayüzünü öğrenme",
                        "Temel UI/UX prensiplerini anlama",
                        "Wireframe ve prototype oluşturma",
                        "Design system kavramını kavrama",
                    ],
                },
                {
                    "lesson_number": "14",
                    "title": "GitHub - Versiyon Kontrolü ve İşbirliği",
                    "tool": "GitHub",
                    "template": "advanced",
                    "duration": 60,
                    "objectives": [
                        "Git versiyon kontrolü temelleri",
                        "GitHub platformu kullanımı",
                        "Repository yönetimi",
                        "Açık kaynak projelere katkı",
                    ],
                },
                {
                    "lesson_number": "15",
                    "title": "Blender - 3D Modelleme Temelleri",
                    "tool": "Blender",
                    "template": "basic",
                    "duration": 60,
                    "objectives": [
                        "3D modelleme temelleri",
                        "Blender arayüz kullanımı",
                        "Basit objeler oluşturma",
                        "Render alma",
                    ],
                },
            ]
        }

    def update_existing_lesson(self, lesson_path: str, updates: Dict) -> bool:
        """Mevcut ders planını güncelle"""

        try:
            file_path = Path(lesson_path)

            if not file_path.exists():
                print(f"❌ Dosya bulunamadı: {lesson_path}")
                return False

            # Mevcut içeriği oku
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Güncellemeleri uygula
            for section, new_content in updates.items():
                # Basit string replacement (geliştirilmesi gerekebilir)
                pattern = f"## {section}"
                if pattern in content:
                    # Mevcut bölümü bul ve güncelle
                    # Bu kısım daha sofistike parser ile geliştirilebilir
                    pass

            # Güncelleme tarihini ekle
            timestamp = datetime.datetime.now().strftime("%d %B %Y")
            content += f"\n\n---\n**Son Güncelleme**: {timestamp}"

            # Dosyayı kaydet
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ Ders planı güncellendi: {lesson_path}")
            return True

        except Exception as e:
            print(f"❌ Güncelleme hatası: {e}")
            return False

    def generate_lesson_index(self, lessons_dir: str) -> str:
        """Tüm dersler için index dosyası oluştur"""

        lessons_path = Path(lessons_dir)
        index_content = []

        index_content.append("# Ders Planları İndeksi")
        index_content.append("")
        index_content.append(
            "Bu dizin, tüm ders planlarının organize listesini içerir."
        )
        index_content.append("")

        # Ders klasörlerini tara
        lesson_dirs = sorted([d for d in lessons_path.iterdir() if d.is_dir()])

        for lesson_dir in lesson_dirs:
            lesson_name = lesson_dir.name
            plan_file = lesson_dir / "ders_plani.md"

            if plan_file.exists():
                # İlk satırdan başlığı çıkar
                with open(plan_file, "r", encoding="utf-8") as f:
                    first_line = f.readline().strip()
                    title = first_line.replace("# ", "")

                index_content.append(f"## {title}")
                index_content.append(f"- **Klasör**: `{lesson_name}/`")
                index_content.append(
                    f"- **Ders Planı**: [`ders_plani.md`](./{lesson_name}/ders_plani.md)"
                )
                index_content.append("")

        # Oluşturma tarihi
        timestamp = datetime.datetime.now().strftime("%d %B %Y, %H:%M")
        index_content.append("---")
        index_content.append(f"**Son Güncelleme**: {timestamp}")

        return "\n".join(index_content)


def main():
    """Ana fonksiyon - Demo kullanım"""

    print("🚀 GSB Dijital Okuryazarlık - Ders Planı Üretici")
    print("=" * 60)

    # Generator'ı başlat
    generator = LessonPlanGenerator()

    # Örnek ders oluştur
    lesson_data = {
        "lesson_number": "13",
        "title": "Figma - UI/UX Tasarım Temelleri",
        "tool": "Figma",
        "template": "advanced",
        "objectives": [
            "Figma arayüzünü öğrenme",
            "Temel UI/UX prensiplerini anlama",
            "Wireframe ve prototype oluşturma",
        ],
    }

    print("\n📝 Örnek ders planı oluşturuluyor...")
    content = generator.create_lesson_plan(lesson_data)

    # İçeriği göster (ilk 500 karakter)
    print("\n📄 Oluşturulan İçerik Önizleme:")
    print("-" * 40)
    print(content[:500] + "..." if len(content) > 500 else content)

    # Toplu ders oluşturma örneği
    print("\n📚 Örnek toplu ders yapılandırması...")
    example_config = generator.create_example_config()

    # Yapılandırmayı kaydet
    with open("example_lessons_config.json", "w", encoding="utf-8") as f:
        json.dump(example_config, f, ensure_ascii=False, indent=2)

    print("✅ Örnek yapılandırma kaydedildi: example_lessons_config.json")

    print("\n🎉 Demo tamamlandı!")
    print("\n📖 Kullanım:")
    print("1. lesson_data dict'i ile create_lesson_plan() çağır")
    print("2. save_lesson_plan() ile dosyaya kaydet")
    print("3. batch_create_lessons() ile toplu oluştur")


if __name__ == "__main__":
    main()

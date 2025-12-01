# GSB Dijital Okuryazarlık Eğitimi - Scripts Rehberi

Bu klasör, GSB Dijital Okuryazarlık Eğitimi projesinin otomatik scriptlerini ve yardımcı araçlarını içerir.

## 📂 Scripts Genel Bakış

### 🐍 Python Scripts

| Script | Açıklama | Kullanım |
|--------|----------|----------|
| `course_tracker.py` | Öğrenci takip sistemi | Katılım ve proje takibi |
| `lesson_generator.py` | Ders planı üretici | Yeni ders planları oluşturma |
| `index_builder.py` | INDEX otomasyon aracı | `python index_builder.py --write` |
| `content_report.py` | Ders içerik raporu | `python content_report.py` |
| `utils.py` | Yardımcı fonksiyonlar | Genel utility işlemleri |

### 🌐 Web Components

| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `dashboard.html` | Web dashboard | İlerleme görselleştirme |

### ⚙️ Configuration

| Dosya | Açıklama | İçerik |
|-------|----------|---------|
| `requirements.txt` | Python dependencies | Gerekli paketler |

---

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler

```bash
# Python 3.8+ gerekli
python --version

# Paketleri yükle
pip install -r requirements.txt
```

### 2. Scripts Çalıştırma

```bash
# Kurs takip sistemi
python course_tracker.py

# Ders planı üretici
python lesson_generator.py

# Utility fonksiyonları test
python utils.py
```

### 3. Web Dashboard

```bash
# HTML dosyasını tarayıcıda aç
start dashboard.html  # Windows
open dashboard.html   # macOS
xdg-open dashboard.html  # Linux
```

---

## 📊 course_tracker.py

### Özellikler
- ✅ Öğrenci kayıt sistemi
- ✅ Katılım takibi
- ✅ Proje durumu yönetimi
- ✅ İlerleme hesaplama
- ✅ Sertifika uygunluk kontrolü
- ✅ CSV rapor dışa aktarma
- ✅ JSON veri saklama

### Kullanım Örnekleri

```python
from course_tracker import CourseTracker

# Tracker'ı başlat
tracker = CourseTracker()

# Öğrenci ekle
student_data = {
    "id": "GSB001",
    "name": "Ahmet Yılmaz",
    "email": "ahmet@email.com",
    "phone": "0555-123-4567",
    "school": "Atatürk Lisesi",
    "grade": 11
}
tracker.add_student(student_data)

# Katılım işaretle
tracker.mark_attendance("GSB001", "01", True)

# Proje durumu güncelle
tracker.update_project_status("GSB001", "01", "completed")

# İlerleme raporu
progress = tracker.calculate_student_progress("GSB001")
print(f"İlerleme: %{progress['overall_progress']}")

# CSV raporu
tracker.export_to_csv()
```

### Veri Yapısı

```python
Student = {
    "id": str,           # GSB001, GSB002, ...
    "name": str,         # Öğrenci adı
    "email": str,        # E-posta adresi
    "phone": str,        # Telefon numarası
    "school": str,       # Okul adı
    "grade": int,        # Sınıf seviyesi
    "attendance": {      # Ders katılımı
        "01": True,      # Ders ID: Katılım durumu
        "02": False,
        # ...
    },
    "projects": {        # Proje durumları
        "01": "completed",
        "02": "in_progress",
        # ...
    },
    "total_score": float # Genel puan
}
```

---

## 📝 lesson_generator.py

### Özellikler
- ✅ Otomatik ders planı oluşturma
- ✅ Template sistemi (basic/advanced)
- ✅ Toplu ders oluşturma
- ✅ Markdown formatı
- ✅ Özelleştirilebilir içerik
- ✅ Mevcut planları güncelleme

### Template Türleri

#### Basic Template
- Ders Amacı
- Süre
- Ders İçeriği
- Pratik Ödevler
- Değerlendirme Kriterleri
- Yararlı Linkler

#### Advanced Template
- Ön Gereksinimler
- İpuçları ve Püf Noktaları
- Teknik Özellikler
- Özel Projeler
- Yaratıcı Uygulamalar

### Kullanım Örnekleri

```python
from lesson_generator import LessonPlanGenerator

# Generator'ı başlat
generator = LessonPlanGenerator()

# Tek ders oluştur
lesson_data = {
    "lesson_number": "13",
    "title": "Figma - UI/UX Tasarım",
    "tool": "Figma",
    "template": "advanced",
    "objectives": [
        "UI/UX prensiplerini öğrenme",
        "Wireframe oluşturma",
        "Prototype tasarımı"
    ]
}

content = generator.create_lesson_plan(lesson_data)
generator.save_lesson_plan(content, "13")

# Toplu ders oluşturma
lessons_config = [
    {
        "lesson_number": "14",
        "title": "GitHub - Versiyon Kontrolü", 
        "tool": "GitHub",
        "template": "basic"
    },
    # ... daha fazla ders
]

generator.batch_create_lessons(lessons_config)
```

### Configuration Format

```json
{
  "lessons": [
    {
      "lesson_number": "13",
      "title": "Tool Name - Description",
      "tool": "ToolName",
      "template": "basic|advanced",
      "duration": 60,
      "objectives": [
        "Learning objective 1",
        "Learning objective 2"
      ]
    }
  ]
}
```

---

## 🧭 index_builder.py

`INDEX.md` dosyasını ders klasörlerini tarayarak otomatik oluşturur. Kullanmadan önce
proje kökünde olduğunuzdan emin olun:

```bash
python index_builder.py --write
```

Bu komut `ders_notlari/` ve `ornek_calisma/` dizinlerini tarar, süre ve hedefleri çıkarır,
eksik plan ya da slaytları da not olarak raporlar.

---

## 📊 content_report.py

Her ders için plan, slayt, dist çıktısı ve örnek çalışma var mı kontrol ederek kısa özet
tablosu çıkarır; istenirse JSON rapor üretir.

```bash
python content_report.py --json-out dist/content_report.json
```

JSON çıktısı CI veya dashboard entegrasyonlarında kullanılabilir; terminal tablosu ise
eksikleri hızlıca görmeyi kolaylaştırır.

---

## 🛠️ utils.py

### Modüller

#### FileManager
```python
from utils import FileManager

# Dizin oluşturma
FileManager.create_directory("new_folder")

# Dosya okuma/yazma
content = FileManager.read_file("file.txt")
FileManager.write_file("output.txt", "içerik")

# Dosya kopyalama
FileManager.copy_file("source.txt", "destination.txt")
```

#### DataValidator
```python
from utils import DataValidator

# Veri doğrulama
is_valid_email = DataValidator.validate_email("test@example.com")
is_valid_phone = DataValidator.validate_phone("0555-123-4567")
is_valid_id = DataValidator.validate_student_id("GSB001")

# Dosya adı güvenli hale getirme
safe_name = DataValidator.sanitize_filename("Öğrenci Listesi.xlsx")
```

#### ExcelExporter
```python
from utils import ExcelExporter

# Öğrenci verilerini CSV'ye aktar
filename = ExcelExporter.export_student_data(students_dict)

# Ders istatistiklerini dışa aktar
stats_file = ExcelExporter.export_lesson_statistics(lessons, attendance)
```

#### MarkdownProcessor
```python
from utils import MarkdownProcessor

# Başlıkları çıkar
headings = MarkdownProcessor.extract_headings(markdown_content)

# İçindekiler oluştur
toc = MarkdownProcessor.create_table_of_contents(markdown_content)

# Link doğrulama
links = MarkdownProcessor.validate_links(markdown_content)
```

#### ConfigManager
```python
from utils import ConfigManager

# Config yükle
config = ConfigManager("settings.json")

# Değer al
course_name = config.get("course.name")
min_attendance = config.get("course.min_attendance_rate", 80.0)

# Değer ata
config.set("notifications.enabled", True)
```

---

## 🌐 dashboard.html

### Özellikler
- 📊 **İlerleme Göstergeleri**: Circular progress, bar charts
- 📈 **İstatistikler**: Öğrenci sayıları, tamamlama oranları
- 📚 **Ders Kartları**: Her ders için detaylı kart
- 🛠️ **Araç Galerisi**: Öğretilen dijital araçlar
- 📱 **Responsive Design**: Mobil uyumlu tasarım
- ✨ **Animasyonlar**: Smooth transitions ve effects

### Teknolojiler
- **HTML5**: Semantic markup
- **CSS3**: Modern styling, Grid, Flexbox
- **JavaScript**: Interactive animations
- **Font Awesome**: Icon library
- **Gradient Backgrounds**: Modern visual design

### Customization
Dashboard'u özelleştirmek için:

```html
<!-- İstatistikleri güncelle -->
<div class="stat-number">12</div>  <!-- Yeni değer -->

<!-- Yeni ders kartı ekle -->
<div class="lesson-card">
  <div class="lesson-header">
    <div class="lesson-number">13</div>
    <div>
      <div class="lesson-title">Yeni Ders</div>
      <div class="lesson-tool">Yeni Araç</div>
    </div>
  </div>
</div>
```

---

## 📋 Veri Formatları

### JSON Veri Yapısı

```json
{
  "students": [
    {
      "id": "GSB001",
      "name": "Student Name",
      "email": "email@example.com",
      "phone": "0555-123-4567",
      "school": "School Name",
      "grade": 11,
      "registration_date": "2024-11-19T10:30:00",
      "attendance": {
        "01": true,
        "02": false
      },
      "projects": {
        "01": "completed",
        "02": "in_progress"
      },
      "total_score": 85.5
    }
  ],
  "last_updated": "2024-11-19T15:45:00"
}
```

### CSV Export Format

```csv
Öğrenci ID,İsim,E-posta,Okul,Sınıf,Katılım Oranı (%),Proje Tamamlama (%),Genel İlerleme (%),Sertifika Uygun
GSB001,Ahmet Yılmaz,ahmet@email.com,Atatürk Lisesi,11,85.0,75.0,80.0,Evet
GSB002,Ayşe Kaya,ayse@email.com,Cumhuriyet Lisesi,10,70.0,65.0,67.5,Hayır
```

---

## 🔧 Troubleshooting

### Yaygın Hatalar

#### ImportError: No module named 'pandas'
```bash
# Çözüm: Gerekli paketleri yükle
pip install -r requirements.txt
```

#### UnicodeDecodeError
```python
# Çözüm: Encoding belirt
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()
```

#### Permission Denied
```bash
# Çözüm: Administrator olarak çalıştır
# veya dosya izinlerini kontrol et
```

### Debug Modu

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Detaylı log mesajları göreceksiniz
```

---

## 🚀 Geliştirme

### Yeni Script Ekleme

1. **Yeni .py dosyası oluştur**
2. **Docstring ekle**:
```python
"""
Script açıklaması
================
Ne yaptığını açıkla

Özellikler:
- Özellik 1
- Özellik 2

Yazar: İsim
Tarih: Tarih
"""
```
3. **Main fonksiyon ekle**:
```python
def main():
    """Ana fonksiyon - Demo kullanım"""
    print("Demo mesajları")

if __name__ == "__main__":
    main()
```
4. **README.md'yi güncelle**

### Code Style

- **PEP 8** Python style guide
- **Type hints** kullan
- **Docstrings** ekle
- **Error handling** yap
- **Logging** kullan

### Testing

```python
def test_function():
    """Test fonksiyonu örneği"""
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
    print("✅ Tüm testler başarılı")
```

---

## 📞 Destek

### Sorun Bildirimi
- GitHub Issues kullanın
- Hata detaylarını ekleyin
- Python version'ınızı belirtin
- Log mesajlarını paylaşın

### Katkıda Bulunma
1. Fork yapın
2. Feature branch oluşturun
3. Kod yazın ve test edin
4. Pull Request gönderin

---

**Son Güncelleme**: 19 Kasım 2024  
**Python Versiyon**: 3.8+  
**Lisans**: MIT
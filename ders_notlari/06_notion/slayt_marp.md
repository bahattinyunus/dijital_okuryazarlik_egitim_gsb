---
marp: true
title: "Notion — Bilgi Yönetimi ve Dijital Ajanda"
description: "GSB Dijital Okuryazarlık Eğitimi — 6. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 6. Ders · Notion"
style: |
  :root {
    --primary: #2F80ED;
    --accent: #F2994A;
    --success: #27AE60;
    --warning: #E2B93B;
    --text: #1F2937;
  }
  section { font-size: 28px; color: var(--text); }
  section.lead h1, section.lead h2, section.lead p { color: #fff; }
  section.lead { background: linear-gradient(135deg, #2F80ED 0%, #56CCF2 100%); }
  h1, h2, h3 { color: var(--primary); }
  strong { color: var(--primary); }
  blockquote { border-left: 6px solid var(--accent); padding-left: 16px; color: #374151; }
  .pill { display: inline-block; padding: 6px 12px; border-radius: 999px; background: #EEF2FF; color: #3730A3; font-weight: 700; }
  .ok { color: var(--success); font-weight: 700; }
  .warn { color: var(--warning); font-weight: 700; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start; }
  ul.tight > li { margin: 6px 0; }
  .kbd { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; background: #F3F4F6; border: 1px solid #E5E7EB; padding: 2px 6px; border-radius: 6px; }
---

<!-- _class: lead -->
# Notion
## Bilgi Yönetimi ve Dijital Ajanda
GSB Dijital Okuryazarlık — 6. Ders

- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Ders sonunda herkes bir “Kişisel Görevler + Notlar” çalışma alanı kurmuş olacak.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Notion’ın blok tabanlı yapısını ve sayfa hiyerarşisini kavrayacaksınız.
- Veritabanlarını (Table/Board/Calendar/List/Gallery/Timeline) kurabileceksiniz.
- Özellikleri (Properties), İlişkiler (Relation) ve Rollup’ları kullanabileceksiniz.
- Şablonlar, bağlantılar, mention ve backlink mantığını uygulayabileceksiniz.
- Kişisel ajanda, görev takibi ve bilgi arşivi kurabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş ve Notion’a bakış
- 15 dk — Sayfa/blok sistemi ve veritabanı temelleri
- 15 dk — Uygulama: Görev + Notlar veritabanları
- 10 dk — İlişkilendirme, görünüm ve filtreler
- 10 dk — Paylaşım, şablonlar, mini vitrin

---

## 🧭 Neden Notion?
- Tek platformda notlar, görevler, veri ve wiki
- Blok tabanlı esnek düzen
- Güçlü veritabanı ve çoklu görünüm
- Şablon ve otomasyonlarla hız
- Ekip işbirliği ve paylaşım esnekliği

> “Bilginizi sistemleştirirseniz, fikir üretmek kolaylaşır.”

---

## 🚪 Başlangıç: Erişim
- notion.so → Ücretsiz hesap
- Masaüstü ve mobil uygulamaları indirilebilir
- Workspace (çalışma alanı) oluşturun
- Kişisel çalışma: “Private” sayfalarla başlayın

İpucu: “GSB – Dijital Ajanda” adında ana sayfa oluşturun.

---

## 🧱 Notion Mantığı: Bloklar ve Sayfalar
- Her şey bir bloktur: Başlık, metin, yapılacaklar, tablo, görsel…
- Slash menü: “/” yazarak blok ekleyin
- İç içe sayfalar: Sayfa içinde sayfa
- Drag & drop ile blokları yeniden sırala, sütun yapısı kur

Temel bloklar:
- Heading 1/2/3, Paragraph, Bulleted/Numbered list
- To-do, Toggle list, Quote, Callout
- Divider, Image, File, Code, Embed

---

## 🗂️ Sayfa Hiyerarşisi ve Navigasyon
- Ana sayfa → Alt sayfalar → Veritabanları
- Breadcrumb: Sayfa yolunu üstte görün
- Favorite: Sık kullanılan sayfaları sabitleyin
- Quick find (.kbd[Ctrl + P]): Her şeyi hızlı arayın

İpucu: “Index” sayfası ile tüm alt içeriklere bağlantı verin.

---

## 🧮 Veritabanı Temelleri
Veritabanları = Satırlar (kayıtlar) + Özellikler (properties) + Görünümler
- Türler: Table, Board (Kanban), Calendar, List, Gallery, Timeline
- Aynı veriyi farklı görünümle izleyin (ör. Table + Calendar)
- Yeni özellik ekleme: Text, Number, Select/Multi-Select, Date, Person, Files & media, Checkbox, URL, Email, Phone, Formula, Relation, Rollup

---

## 🧩 Properties (Özellikler) — Örnekler
Görev veritabanı:
- Title: Görev adı
- Status: Select (To Do, Doing, Done)
- Priority: Select (Low/Med/High)
- Due: Date
- Assignee: Person
- Tags: Multi-Select
- Done?: Checkbox
- Link: URL

Notlar veritabanı:
- Title: Not başlığı
- Topic: Select
- Source: URL
- Related Task: Relation (Görev DB ile)
- Excerpt: Text

---

## 🔗 Relation ve 🔁 Rollup
- Relation: İki veritabanı arasında bağlantı (ör. Not ↔ Görev)
- Rollup: Relation üzerinden bağlı veriden özet bilgi getirme
  - Örn: “İlişkili not sayısı”, “İlişkili görevlerin tamamlanma oranı”
- Senaryo:
  - Notlar DB → Related Task (Relation)
  - Görevler DB → Related Notes (Relation)
  - Görevler DB → Notes Count (Rollup → Count)

Avantaj: Bağlantılı bilgi tek ekranda.

---

## 🧭 Görünümler: Table, Board, Calendar, List, Gallery, Timeline
- Table: Veri odaklı tablo
- Board: Kanban akışı (Status sütunlarına göre)
- Calendar: Tarih tabanlı planlama
- List: Minimal liste görünümü
- Gallery: Kart görünümleri (kapak + özet)
- Timeline: Süre/bağımlılık (ileri kullanım)

Filtre ve Sıralama:
- Filter: “Status ≠ Done”, “Assignee = Ben”
- Sort: “Due artan”, “Priority High → Low”

---

## 🧪 Uygulama 1 — Görev Veritabanı
Hedef: Basit görev takip sistemi
- Yeni veritabanı → Table → “Tasks”
- Properties: Status, Priority, Due, Assignee, Tags, Done?
- Board View: Status’a göre (To Do/Doing/Done)
- Calendar View: Due tarihine göre
- Filtre: “Assignee = Me” veya “Done? = Unchecked”

Kontrol: 6 görev girin, 1’ini Done’a taşıyın.

---

## 🧪 Uygulama 2 — Notlar Veritabanı
Hedef: Konu bazlı not arşivi
- Yeni veritabanı → Table → “Notes”
- Properties: Topic (Select), Source (URL), Related Task (Relation → Tasks)
- Gallery View: Kapak görselli not koleksiyonu
- List View: Minimal okuma akışı
- Rollup (Tasks DB): “Related Notes” → Count

Kontrol: En az 4 not girin, 2’sini görevlere bağlayın.

---

## 🗓️ Kişisel Ajanda ve Haftalık Görünüm
- Weekly Dashboard sayfası oluşturun
- Embed: Calendar görünümünü ekleyin
- Linked Database: “/Create linked view of database” ile Tasks/Notes görünümlerini bu sayfaya bağlayın
- Filtre: Haftaya ait görevler, yeni notlar
- Checklist: Haftalık hedefler

İpucu: “Review” bölümü ile haftalık değerlendirme soruları ekleyin.

---

## 📦 Şablonlar (Templates)
- Veritabanı satır şablonları (ör. Görev kartı standart alanlar)
- Sayfa şablonları (Toplantı notu, proje planı)
- Global şablonlar: Notion Template Gallery
- Tekrarlayan içerikler için hız kazandırır

Örnek: “Toplantı Notu” şablonu → Tarih, Katılımcılar, Gündem, Kararlar, Aksiyonlar.

---

## 🧭 Backlinks, Mention ve Bağlantılar
- @mention: Kişi, sayfa, tarih
- Backlinks: Bir sayfaya link verdiğinizde karşı sayfada “Backlinks” görünür
- Wiki mantığı: Kavram sayfaları açın, her yerden link verin
- İçindekiler (Table of Contents): Uzun sayfalar için gezinme

İpucu: “Sözlük/Glosary” sayfası ile kavramları tek yerde toplayın.

---

## 👥 Paylaşım ve Ekip Çalışması
- Share: Bağlantı ile paylaşım, erişim düzeyi (Can view / Can comment / Can edit)
- Davet: E-posta ile kişi ekleme
- Çalışma alanı izinleri: Özel sayfaları Private tutun
- Yorumlar ve tartışma: Satır içi yorumlar, karar kayıtları

Güvenlik: Gereksiz “Public” erişimden kaçının.

---

## ⌨️ Yararlı Kısayollar
- Hızlı arama: .kbd[Ctrl + P]
- Yeni sayfa: .kbd[Ctrl + N]
- Kopyala blok: .kbd[Ctrl + D]
- Satır yukarı/aşağı taşı: .kbd[Ctrl + Shift + ↑/↓]
- Tam ekran: .kbd[Ctrl + Shift + F]
- Slash menü: “/” ile blok listesi

Not: Mac’te .kbd[Ctrl] yerine .kbd[Cmd].

---

## ⚙️ Export / Import ve Entegrasyonlar
- Export: Markdown/HTML/PDF (sayfa/veritabanı)
- Import: Markdown, CSV, bazı dış platformlar
- Embed: Google Drive dosyaları, YouTube, Figma, Miro vb.
- Web clipper: Tarayıcı eklentisi ile sayfayı hızlı kaydet

İpucu: Veritabanı → “Export as CSV” ile dış analiz.

---

## ♿ Erişilebilirlik ve Düzen
- Başlık hiyerarşisi (H1→H2→H3)
- Alternatif metin (görsel açıklamaları)
- Kontrast ve sade renkler
- Okunabilir font/boşluklar
- İsimlendirme standartları: Kısa ve açıklayıcı

---

## 🔒 Gizlilik ve Yedekleme
- Erişim kontrolü: Kişi/Grup bazlı yetkiler
- Versiyon geçmişi: Değişiklikleri geri al
- Kopya sayfa: “Duplicate” ile versiyonlama
- Dışa aktarma: Periyodik yedek (Markdown/CSV)

---

## 🧪 Uygulama — 12 Dakika
Görev:
- “GSB – Dijital Ajanda” ana sayfası
- “Tasks” ve “Notes” veritabanlarını oluşturun
- Relation: Notes → Related Task
- Görünüm: Tasks için Board + Calendar, Notes için Gallery
- Haftalık Dashboard sayfasında linked view ile özet
- En az 6 görev, 4 not ekleyin, 2 bağı ilişkilendirin

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Değerlendirme Kontrol Listesi
- [ ] Ana sayfa ve sayfa hiyerarşisi kuruldu
- [ ] Tasks ve Notes veritabanları oluşturuldu
- [ ] Relation + Rollup uygulandı
- [ ] Görünümler (Board/Calendar/Gallery) ayarlandı
- [ ] Filtre ve sıralama kullanıldı
- [ ] Haftalık Dashboard hazır
- [ ] En az 2 not görevle ilişkilendirildi

---

## 🧰 Kaçınılacaklar ve İpuçları
Kaçınılacaklar:
- Aşırı karmaşık yapı, gereksiz özellik kalabalığı
- Standartsız isimlendirme ve etiketler
- Filtre/sıralama olmadan “her şey tek listede” bırakmak

İpuçları:
- Küçük başlayın, iteratif geliştirin
- Şablonlar ile standartlaştırın
- Haftalık gözden geçirme rutini ekleyin

---

## 🔗 Yararlı Kaynaklar
- Notion Help Center: https://www.notion.so/help
- Template Gallery: https://www.notion.so/templates
- Notion Web Clipper: https://www.notion.so/web-clipper
- Resmi YouTube Kanalı: https://www.youtube.com/@NotionHQ

---

## 🧭 Sonraki Adım (Ödev)
- Kişisel “Second Brain” iskeleti:
  - Areas (Alanlar), Projects (Projeler), Resources (Kaynaklar), Archive
  - Tasks ↔ Notes ilişkilerini genişletin
- 1 proje seçin → Hedefler, görevler, referans notlar
- Haftalık rapor sayfası ile öz değerlendirme

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 gönüllü Dashboard’unu gösterir (60 sn)
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve iyileştirme alanları

::: notes
Kısa ve somut örnekler seçin; iyi uygulamaları görünür kılın.
:::

---

## ❓ Soru-Cevap
- Veritabanı ve ilişkilendirme senaryoları
- Görünümler ve filtreleme ipuçları
- Şablonlar ve paylaşım stratejileri

Teşekkürler! Bilginizi sistemleştirmek için güçlü bir temel attınız. 🚀
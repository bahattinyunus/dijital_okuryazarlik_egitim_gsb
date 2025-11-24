---
marp: true
title: "Google Formlar — Anket ve Quiz Oluşturma"
description: "GSB Dijital Okuryazarlık Eğitimi — 4. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 4. Ders · Google Formlar"
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
# Google Formlar
## Anket ve Quiz Oluşturma
GSB Dijital Okuryazarlık — 4. Ders

- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Ders sonunda herkes bir sınıf profili anketi ve kısa bir quiz taslağı hazırlamış olacak.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Google Formlar arayüzünü ve soru türlerini tanıyacaksınız.
- Mantık atlaması (branching) ve yanıt doğrulama uygulayabileceksiniz.
- Quiz modunda puanlama ve cevap anahtarı oluşturabileceksiniz.
- Yanıtları analiz edip Google Sheets’e aktarabileceksiniz.
- Formu bağlantı/QR/yerleştirme ile paylaşabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş ve kullanım alanları
- 15 dk — Arayüz turu ve soru türleri
- 15 dk — Uygulama: Sınıf profili anketi
- 10 dk — Quiz modu, doğrulama, mantık atlaması
- 10 dk — Paylaşım, yanıt analizi, mini vitrin

---

## 🧭 Neden Google Formlar?
- Kolay ve hızlı anket/quiz tasarımı
- Otomatik grafikli analiz ve özet görünüm
- Google Sheets ile güçlü veri işleme
- Paylaşım ve dağıtımda esneklik (link, QR, embed)
- Ücretsiz ve erişilebilir

> “Doğru sorular, doğru veriyi getirir.”

---

## 🚪 Başlangıç: Erişim
- forms.google.com → Yeni form başlat
- Drive → Yeni → Google Formlar
- Şablon Galerisi: Hazır temalardan başlayın
- Proje klasörü: “GSB_Forms” ile düzen sağlayın

İpucu: Konuya uygun şablon seçmek süreyi kısaltır.

---

## 🖥️ Arayüz Turu (Hızlı Bakış)
- Sol: Soru listesi ve bölümler
- Orta: Seçili sorunun içerik alanı
- Sağ: Soru türleri, tema, önizleme, ayarlar
- Üst: Form adı, açıklama, “Yanıtlar” sekmesi

İlk iş: Form adını ve kısa açıklamayı girin.

---

## 🧩 Soru Türleri — Genel Bakış
- Metin: Kısa Yanıt, Paragraf
- Seçim: Çoktan Seçmeli, Onay Kutuları, Açılır Liste
- Ölçek/Izgara: Doğrusal Ölçek, Çoklu Seçim/Onay Izgarası
- Tarih/Saat
- Dosya yükleme
- Görsel/Video ekleme (soruya bağlanabilir)

Not: Her soruda “Zorunlu” seçeneğini ihtiyaca göre işaretleyin.

---

## 🧪 Mini Proje 1 — Sınıf Profili Anketi
Hedef: Sınıfı hızlıca tanıyalım (8–10 soru)
- İsim (Kısa yanıt) — zorunlu
- E-posta (Kısa yanıt + doğrulama)
- Sınıf/Yaş (Açılır liste)
- İlgi alanları (Onay kutuları)
- Okul etkinliklerine ilgi (Doğrusal ölçek)
- Açık uçlu öneri (Paragraf)

Teslim: Bağlantı ve QR ile paylaşın.

---

## ➕ Soru Ekleme ve Düzenleme
- Soru ekle: Sağ menüde “+”
- Kopyala/Sil: Soru kartındaki ikonlar
- Zorunlu: Anahtar işaretini aktif edin
- Yardım metni: Soruya ipucu ekleyin
- Seçenekleri sürükle-bırak ile sıralayın

İpucu: Soru numaralandırması yerine kısa, net başlıklar kullanın.

---

## 🖼️ Görsel ve Video Soruları
- Görsel ekle: Soruya küçük görsel ekleyin
- Video: YouTube linkiyle soru bağlamı verin
- Görsel/Video kartına açıklama yazın
- Kullanım alanı: Görsel tanıma, kısa video sonrası soru

---

## 🧱 Bölümler ve Mantık Atlama (Branching)
- Bölüm ekle: Formu sayfalara ayırır
- “Sorunun yanıtına göre bölüm atla” → dallanma
- Senaryo: “Hangi etkinliği istersin?” → Seçime göre farklı bölüm
- “İleri/Önceki” akışını test edin

Not: Uzun formlarda terk oranını azaltır.

---

## ✅ Yanıt Doğrulama Örnekleri
- E-posta formatı: “@” ve domain kontrolü
- Sayısal aralık: 1–10 arası
- Karakter uzunluğu: Min/Max
- RegEx: Özel desenler (ileri kullanım)

İpucu: Doğrulama mesajını kullanıcı dostu yazın.

---

## 🧪 Mini Proje 2 — Kısa Quiz
Hedef: 5 soruluk otomatik puanlanan quiz
- Ayarlar → Quizler → Bu formu quiz yap
- Her soruya doğru cevap ve puan atayın
- Geri bildirim metni: Doğru/yanlış için ipuçları
- Puan gösterimi: Gönderim sonrası görünürlük ayarları

---

## 👥 Paylaşım ve Dağıtım
- Gönder → Link kısalt → Paylaş
- E-posta ile davet
- QR kod: Linki QR’a dönüştürün (harici üretici)
- Web’e yerleştirme (Embed): <iframe> ile siteye gömün
- Organizasyon kısıtları: Sadece kurum hesaplarıyla sınırla

Güvenlik: Gerekmedikçe “Herkes”e açık yapmayın.

---

## 📊 Yanıtlar Sekmesi ve Sheets Entegrasyonu
- Özet: Grafikler, ortalamalar
- Soru bazlı ve bireysel yanıtlar
- Sheets’e bağla: “Yeşil” simge
- Canlı veri: Yeni yanıtlar otomatik işler
- İndirme: CSV ile dışa aktarım

İpucu: Analiz için önceden sütun adlarını planlayın.

---

## 📈 Temel Analiz ve Görselleştirme
- Katılımcı sayısı, tamamlama oranı
- Çoktan seçmeli → Pasta/çubuk grafik
- Ölçek soruları → Ortalama/dağılım
- Açık uçlu → Anahtar kelimeler (manuel/ek araç)
- A/B test: İki form varyasyonunun sonuçlarını kıyaslayın

---

## 🔒 Gizlilik ve Güvenlik
- Yanıt limiti: Bir kişi bir yanıt
- Oturum zorunluluğu: Yalnızca giriş yapan yanıtlasın
- Yanıt düzenleme: Gönderim sonrası izin ver/verme
- Kişisel veriler: GDPR/yerel mevzuata uygun toplayın
- Erişim: Link kapsamını düzenli kontrol edin

---

## ⌨️ Yararlı Kısayollar
- Önizleme: .kbd[Ctrl + Enter]
- Kopya soru: Soru kartındaki kopyala ikonu
- Temayı aç: Üst araç çubuğu → “Temayı özelleştir”
- Geri al / yinele: .kbd[Ctrl + Z] / .kbd[Ctrl + Y]

Not: Mac’te .kbd[Ctrl] yerine .kbd[Cmd].

---

## 🧪 Uygulama — 12 Dakika
Görev:
- 1 form: Sınıf profili (8–10 soru)
- 1 bölüm + 1 mantık atlaması
- En az 1 doğrulama (e-posta veya sayı)
- Quiz modunda 2 soru ve puanlama
- Önizleme ve test gönderimi
- Linki sınıfla paylaşın

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Kontrol Listesi
- [ ] Form adı ve açıklaması
- [ ] 3+ farklı soru türü
- [ ] En az 1 zorunlu soru
- [ ] Mantık atlaması çalışıyor
- [ ] Yanıt doğrulaması test edildi
- [ ] Quiz puanlaması tanımlı
- [ ] Yanıtlar Sheets’e aktarıldı

---

## ⚡ Hızlı Başlangıç Şablonları
5 Dakikalık Form:
1) İsim (kısa yanıt)
2) E-posta (doğrulama)
3) Memnuniyet (1–5 ölçek)
4) Öneri (paragraf)

10 Dakikalık Quiz:
- 4 çoktan seçmeli + 1 doğru/yanlış
- Otomatik puanlama açık

---

## 🌟 Yaratıcı Kullanım Örnekleri
- Etkinlik kayıt ve geri bildirim formları
- Mini pazar araştırmaları
- Dallanmalı “seç ve ilerle” hikayeler
- Atölye yoklaması + quiz
- Kulüp başvuruları ve arşiv

---

## 📤 Dışa Aktarma ve İçe Aktarma
- Yanıtları CSV → Excel/Sheets’te analiz
- Formu kopyala: Şablon üret
- Soruları içe aktar: Diğer formlardan soruları çek
- PDF olarak form görüntüsü (tarayıcı baskı)

İpucu: Standart şablonlar zaman kazandırır.

---

## 🧰 Kaçınılacaklar
- Çok uzun formlar → Bölümlere ayırın
- Belirsiz ifadeler → Net ve tek anlamlı yazın
- Zorunlu fazlalığı → Sadece gerekli soruları zorunlu yapın
- Güvenlik açıları → Erişim ve veri alanlarını gözden geçirin

---

## 🔗 Yararlı Kaynaklar
- Google Forms Yardım: https://support.google.com/docs/answer/6281888
- Quiz Oluşturma: https://support.google.com/docs/answer/7032287
- Tasarım İpuçları: https://blog.google/products/forms/form-design-best-practices/
- QR Oluşturucu: https://www.qr-code-generator.com/

---

## 🧭 Sonraki Adım (Ödev)
- “Okul Memnuniyet” anketini 12–15 soruya genişletin
- Mantık atlaması + doğrulama ekleyin
- Sonuçları Sheets’e aktarıp 3 grafik oluşturun
- Kısa bir rapor (Google Docs) ile bulguları özetleyin

---

## ❓ Soru-Cevap
- Soru yazım teknikleri
- Quiz ayarları ve puanlama
- Paylaşım ve erişim kısıtları
- Analiz ve raporlama

Teşekkürler! Doğru tasarlanmış formlarla güçlü veriler toplamaya hazırsınız. 🚀
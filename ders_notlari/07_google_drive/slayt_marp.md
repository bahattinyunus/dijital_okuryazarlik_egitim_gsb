---
marp: true
title: "Google Drive — Dosya Yönetimi ve Depolama"
description: "GSB Dijital Okuryazarlık Eğitimi — 7. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 7. Ders · Google Drive"
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

# Google Drive

<div class="card" style="margin-top: 12px;">
  <div class="pill">GSB Dijital Okuryazarlık</div>
  <h2 style="margin: 10px 0 4px;">Dosya Yönetimi ve Depolama</h2>
  <p style="margin: 0; color: #374151;">7. Ders · Süre: 60 dk · Seviye: Başlangıç · Uygulamalı</p>
</div>
## Dosya Yönetimi ve Depolama

GSB Dijital Okuryazarlık — 7. Ders

- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Hedef: Her öğrenci düzenli bir klasör yapısı kuracak, paylaşım ayarlarını öğrenecek ve dosyalarını güvenle yönetebilecek.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Google Drive arayüzünü ve temel kavramları tanıyacaksınız.
- Klasör yapısı kurarak dosyalarınızı düzenleyebileceksiniz.
- Paylaşım ve izinleri doğru şekilde uygulayabileceksiniz.
- Arama, filtre ve kısayollarla hızlı erişim sağlayabileceksiniz.
- Sürüm geçmişi, offline ve yedekleme seçeneklerini kullanabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş ve arayüz turu
- 15 dk — Organizasyon: Klasör, adlandırma, kısayol
- 15 dk — Paylaşım ve izinler, paylaşılan sürücüler
- 10 dk — Sürüm geçmişi, offline, Drive for desktop
- 10 dk — Uygulama ve mini vitrin

---

## 🧭 Neden Google Drive?
- Bulut tabanlı depolama: Her yerden erişim
- Gerçek zamanlı işbirliği (Docs/Sheets/Slides)
- Otomatik kaydetme ve güçlü arama
- Paylaşım ve erişim kontrolü
- Mobil ve masaüstü entegrasyon

> “Düzenli Drive = Hızlı üretkenlik.”

---

## 🚪 Başlangıç: Erişim
- Web: drive.google.com
- Mobil: iOS/Android “Google Drive”
- Masaüstü: “Drive for desktop” (indir → oturum aç)
- Alan kontrolü: Sol alt “Depolama”

İpucu: Kişisel ve okul/kurumsal hesapları karıştırmayın.

---

## 🖥️ Arayüz Turu (Hızlı Bakış)
- Sol menü: Benimle paylaşılan, Son, Yıldızlı, Çöp Kutusu, Depolama
- Orta alan: Klasör ve dosya listesi/kart görünümü
- Üst: Arama çubuğu, filtre/çipler, ayarlar, hesap
- Sağ panel: Ayrıntılar ve etkinlik geçmişi

İlk iş: “GSB_Egitim” üst klasörü oluşturun.

---

## 🗂️ Organizasyon — Klasör Yapısı
Önerilen iskelet:
- 01_Dokumanlar
- 02_Sunumlar
- 03_Gorseller
- 04_Videolar
- 05_Projeler
- 99_Arsiv

İpucu: Klasörlere renk vererek (sağ tık → Renk) görsel ayrıştırma yapın.

---

## 🏷️ Adlandırma Standartları
- Tarih bazlı: 2024-11-24_toplanti-notlari.docx
- Versiyon: rapor_v1.pdf, rapor_v2.pdf
- Kısa ve açıklayıcı: projeA_sunum_final.pptx
- Türkçe karakter ve boşluk yerine “-” veya “_”

Kural: Aynı standart tüm ekipte geçerli olsun.

---

## 🔎 Arama ve Filtreler
- Üst arama çubuğunda “çipler” ile filtreleyin:
  - Tür: Belge, E-Tablo, Sunu, PDF, Resim
  - Sahip: Ben / Diğer
  - Konum: Drive, Benimle paylaşılan, Paylaşılan sürücüler
  - Tarih: Öncesi/sonrası
- Operatörler:
  - type:presentation
  - owner:me
  - before:2024-12-31
  - is:starred

---

## 🔗 Kısayollar ve Çok Konum
- Kısayol oluştur: Sağ tık → “Kısayol ekle Drive’a”
- Aynı dosyaya birden çok klasörden erişim
- Değişiklik tek dosyada geçerli

Not: Kısayollar, eski “birden çok konuma ekleme” davranışının yerini alır.

---

## 📤 Yükleme ve Dönüştürme
- Dosya yükle: Sürükle-bırak veya “Yeni → Dosya yükleme”
- Klasör yükle: “Yeni → Klasör yükleme”
- Google formatına dönüştürme:
  - Ayarlar → “Dosyaları yüklerken dönüştür”
  - DOCX → Google Dokümanlar (isteğe bağlı)
- Önizleme: PDF/Resim/Video hızlı görüntüleyin

---

## 👥 Paylaşım ve İzinler
Roller:
- Görüntüleyici (view)
- Yorumcu (commenter)
- Düzenleyici (editor)

Bağlantı paylaşımı:
- Kısıtlı (sadece davet edilenler)
- Bağlantıya sahip olanlar
- Kurum içi (okul/iş hesabı olanlar)

İpucu: Gereksiz “Bağlantıya sahip olan herkes” kullanımından kaçının.

---

## 🧰 Paylaşılan Sürücüler (Workspace)
- Dosyaların sahibi ekip/sürücüdür (kişi değil)
- Ekip bazlı erişim: Yöneticiler, İçerik yöneticileri, Katkıda bulunanlar
- Uzun soluklu proje/ekip çalışmaları için idealdir
- Taşıma: Kişisel → Paylaşılan sürücü (izinlere dikkat)

Not: Bazı özellikler kurumsal hesap gerektirir.

---

## 🕓 Sürüm Geçmişi ve Geri Yükleme
Google dosyaları (Docs/Sheets/Slides):
- Dosyayı aç → Dosya → Sürüm geçmişi
- Sürümleri adlandır, önceki sürüme dön

Diğer dosyalar (PDF, PNG, vb.):
- Drive’da dosyaya sağ tık → “Sürümleri yönet”
- Yeni sürüm yükle, eski sürümleri görüntüle

---

## 🌐 Offline Çalışma
Seçenekler:
- Drive web → Ayarlar → “Çevrimdışı”yı etkinleştir
- Drive for desktop:
  - “Stream” (disk alanı tasarrufu)
  - “Mirror” (tam kopya, offline erişim)

İpucu: Sık çalıştığınız klasör/dosyaları offline önbelleğe alın.

---

## 💻 Drive for desktop (Masaüstü)
- Yerel sürücü harfi (Windows) / Finder (macOS) içinde sanal disk
- Dosyaları PC uygulamalarıyla açıp kaydedin
- Otomatik eşitleme ve sürüm yönetimi
- Yedekleme: Belirli klasörleri Drive’a yansıtın

Dikkat: Ortak bilgisayarlarda oturumu kapatmayı unutmayın.

---

## 🔒 Güvenlik ve Gizlilik
- 2 Adımlı Doğrulama (2FA) aktif olsun
- Paylaşım kapsamlarını düzenli gözden geçirin
- Hassas dosyalarda editör sayısını sınırlayın
- Erişim kaldırma: “Paylaş” → Kullanıcıyı kaldır
- Çöp Kutusu: 30 gün içinde geri alın, sonra kalıcı silinir

---

## ⌨️ Yararlı Kısayollar
- Arama: .kbd[/]
- Yeniden adlandır: .kbd[n]
- Yıldız ekle/çıkar: .kbd[s]
- Ayrıntılar paneli: .kbd[i]
- Kısayol ekle: .kbd[Shift + Z]
- Yeni Doküman: .kbd[Shift + T]
- Yeni E-Tablo: .kbd[Shift + S]
- Yeni Sunu: .kbd[Shift + P]
- Yardım / Kısayollar: .kbd[?]

Not: Mac’te .kbd[Ctrl] yerine .kbd[Cmd] kullanılabilir (belge içi işlemlerde).

---

## 🧪 Uygulama — 12 Dakika
Görev:
- “GSB_Egitim” klasörü ve alt yapıyı oluşturun
- 3 dosya yükleyin (PDF/JPG/PPTX)
- 1 Google Dokümanı oluşturun (toplanti-notu)
- 1 dosyayı sınıfla “Görüntüleyici” yetkisiyle paylaşın
- 1 dosyaya kısayol oluşturup farklı klasöre ekleyin
- 1 dosya sürümünü güncelleyin (yeni sürüm yükleyin)
- Offline erişimi etkinleştirin (en az 1 dosya)

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Değerlendirme Kontrol Listesi
- [ ] Klasör yapısı kuruldu
- [ ] Dosya/klasör yüklendi
- [ ] Paylaşım ve izinler doğru ayarlandı
- [ ] Kısayol kullanıldı
- [ ] Sürüm geçmişi denendi
- [ ] Offline erişim aktifleştirildi
- [ ] Arama/filtre ile dosya bulundu

---

## 🧰 Kaçınılacaklar ve İpuçları
Kaçınılacaklar:
- “Herkes erişebilir” paylaşımları kalıcı bırakmak
- Versiyon adlarını takip etmemek
- Rastgele adlandırma, düzensiz klasörler

İpuçları:
- Haftalık 5 dk bakım (temizlik/arsiv)
- Yıldızlı öğeler ile hızlı erişim
- Paylaşılan sürücülerde rol bazlı erişim

---

## 🔗 Yararlı Kaynaklar
- Google Drive Yardım: https://support.google.com/drive/
- Drive for desktop indir: https://www.google.com/drive/download/
- Paylaşım rehberi: https://support.google.com/drive/answer/2494822
- Kısayollar: https://support.google.com/drive/answer/2563044
- Offline kullanım: https://support.google.com/drive/answer/2375012
- Sürümler: https://support.google.com/drive/answer/2409045

---

## 🧭 Sonraki Adım (Ödev)
- Kişisel Drive’ınızı gözden geçirin:
  - Adlandırma standartlarını uygulayın
  - 1 haftalık “temizlik ve arşiv” yapın
  - En az 1 paylaşılan klasörü ekip arkadaşınızla test edin
- Güvenlik: 2FA aktif, paylaşımları tarayın
- Bir sonraki ders: Siber Güvenlik Temelleri — hesap güvenliği ve veri koruma

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 öğrenci klasör yapısını ve paylaşım ayarlarını gösterir (60 sn)
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve iyileştirme alanları

::: notes
İyi örnekleri görünür kılın; basit ve tutarlı düzeni teşvik edin.
:::

---

## ❓ Soru-Cevap
- Paylaşım/izin senaryoları
- Offline ve Drive for desktop kullanımı
- Sürüm/geri yükleme stratejileri


Teşekkürler! Düzenli Drive ile verimliliğiniz artacak. 🚀

---

## 📸 Görsel Vitrin (Örnek Slaytlar)

<div class="grid-3">
  <figure>
    <img src="https://images.unsplash.com/photo-1529101091764-c3526daf38fe?w=1200&q=80&auto=format&fit=crop" alt="Kapak örneği" class="rounded shadow">
    <figcaption>Kapak — Gradient arkaplan + güçlü başlık</figcaption>
  </figure>
  <figure>
    <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200&q=80&auto=format&fit=crop" alt="İçerik örneği" class="rounded shadow">
    <figcaption>İçerik — 2 sütun düzen + ikonlar</figcaption>
  </figure>
  <figure>
    <img src="https://images.unsplash.com/photo-1529336953121-adffdf0f7fbf?w=1200&q=80&auto=format&fit=crop" alt="Görsel ağırlıklı slayt" class="rounded shadow">
    <figcaption>Görsel — Görsel odaklı anlatım</figcaption>
  </figure>
</div>

---

## 🖼️ Tam Genişlik Görsel

<img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&q=80&auto=format&fit=crop" alt="Tam genişlik slayt örneği" class="full-bleed rounded shadow">

<div class="note">
Bu slaytı, Drive düzeni ve paylaşım kurallarını vurgulayan kısa bir mesajla kullanın (maks. 1 satır).
</div>

---

## 💡 İkonlu İpuçları

- 📁 Klasör hiyerarşisi: “01_Dokumanlar / 02_Sunumlar / 03_Gorseller …” gibi net yapı kur
- 🏷️ Adlandırma: Tarih_İsim_Versiyon (örn. 2024-11-24_toplanti-notu_v2)
- ⭐ Hızlı erişim: Yıldızlı öğelerle sık kullandıklarını öne al
- 🔗 Kısayol: Tek dosyayı birden çok yerde göstermek için kısayol kullan
- 🔒 Paylaşım: “Kısıtlı → davetliler” öncelikli; “Bağlantıya sahip”i gereksiz kullanma
- 🕓 Sürüm: Google dosyalarında sürüm geçmişini adlandırarak takip et
- 🌐 Offline: Önemli klasörleri çevrimdışı önbelleğe al (Drive for desktop)
- ♻️ Arşiv: “99_Arsiv” klasörü ile düzenli temizlik yap

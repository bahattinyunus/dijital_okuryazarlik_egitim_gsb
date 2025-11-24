---
marp: true
title: "Siber Güvenlik — Temeller ve İyi Uygulamalar"
description: "GSB Dijital Okuryazarlık Eğitimi — 8. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 8. Ders · Siber Güvenlik"
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
# Siber Güvenlik
## Güvende Kalmanın Temelleri
GSB Dijital Okuryazarlık — 8. Ders

- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Ders sonunda herkes: güçlü parola + 2FA, phishing ayırt etme, cihaz/ağ güvenliği ve yedekleme konusunda uygulanabilir bir planla çıkacak.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Güçlü parola oluşturup güvenli şekilde yönetebileceksiniz.
- 2FA/MFA etkinleştirme adımlarını uygulayabileceksiniz.
- Phishing ve sosyal mühendislik saldırılarını ayırt edebileceksiniz.
- Cihaz, ağ ve veri güvenliği için temel önlemleri alabileceksiniz.
- Olay anında doğru adımları takip edebileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Tehditler ve temel kavramlar
- 15 dk — Parola hijyeni ve 2FA
- 15 dk — Phishing ve sosyal mühendislik
- 10 dk — Cihaz/Ağ/Veri güvenliği
- 10 dk — Uygulama, kontrol listesi ve kaynaklar

---

## 🧭 Neden Siber Güvenlik?
- Kimlik hırsızlığı ve hesap ele geçirme
- Dolandırıcılık ve veri sızıntıları
- Kişisel itibar ve dijital ayak izi
- Eğitim/iş hayatında kalıcı etkiler

> “Güvenlik bir ürün değil, süreçtir.” — Sürekli dikkat ve alışkanlıklar

---

## 🔑 Parola Hijyeni — Temeller
- Uzunluk: En az 12–14 karakter
- Karışım: Büyük/küçük harf, rakam, sembol
- Benzersizlik: Her hesap için farklı parola
- Şifre yöneticisi kullanımı (parola kasası)
- Parola yerine “parola cümlesi” (ör: “LiseYolunda!2025+Koş”)

.kbd[Asla]:
- Aynı parolayı tekrar kullanmayın
- Ad/soyad/doğum tarihi gibi kolay tahmin edilebilir kalıplar

---

## 🧰 Parola Yöneticileri — İyi Uygulamalar
- Tek güçlü Ana Parola + 2FA
- Otomatik güçlü parola üretimi
- Cihazlar arası senkronizasyon
- Parola sızıntısı denetimi (ihlal uyarıları)
- Acil durum erişimi (güvenilir kişi/plan)

İpucu: Ana parolanızı ezbere bilin, kimseyle paylaşmayın.

---

## 🛡️ 2FA/MFA — İkinci Kalkan
- Yöntemler:
  - Doğrulama uygulaması (TOTP) — önerilir
  - Donanım anahtarı (U2F/FIDO) — en güvenlisi
  - SMS — son çare
- Kurtarma kodlarını güvenle saklayın
- Öncelikli hesaplar: E-posta, sosyal medya, bankacılık, bulut depolama

.kbd[Hemen]: En az 3 kritik hesabınıza 2FA açın.

---

## 🎭 Phishing (Kimlik Avı) — Nasıl Anlaşılır?
- Gönderen adresi: Garip alan adları, harf değiş-tokuşu
- Aciliyet: “Hemen tıkla!”, “Hesabın kapanacak!”
- Linkler: Üstüne gel → Görünen adresle uyuşuyor mu?
- Ekler: Beklenmeyen .exe, .scr, .js, .docm (makrolu) dosyalar
- Yazım/dil bilgisi hataları, sıra dışı talepler

.kbd[TİKLA] yerine: Tarayıcıdan kendin siteye gir ve kontrol et.

---

## 🕵️ Sosyal Mühendislik — Senaryolar
- “IT’den arıyorum, şifreni doğrular mısın?”
- “Ödül kazandın! Bilgilerini gönder.”
- “Arkadaşınmış gibi” DM/WhatsApp mesajları
- Kargo, vergi iadesi, banka aramaları

Savunma:
- Kimlik doğrulaması yapmadan bilgi paylaşma
- Resmi kanallardan geri dön (numarayı sen ara)
- Şüphe → Doğrula → Öyle hareket et

---

## 👣 Dijital Ayak İzi ve Gizlilik
- Paylaşım öncesi düşün: Konum, belge, foto EXIF
- Uygulama izinleri: Kamera/Mikrofon/Depolama
- Profil gizlilik ayarlarını gözden geçir
- Veri minimizasyonu: Gerekenden fazlasını verme
- Hesapları düzenli tarama: Bağlı cihazlar/oturumlar

İpucu: “Herkese açık” paylaşımları minimumda tutun.

---

## 💻 Cihaz Güvenliği — Temel Adımlar
- İşletim sistemi ve uygulamaları güncel tut
- Yalnızca resmi mağazalardan uygulama yükle
- Güvenlik yazılımı (antivirüs/antimalware)
- Ekran kilidi ve otomatik kilit süresi
- Disk şifreleme (BitLocker/FileVault benzeri)
- USB belleklerde otomatik çalıştırmayı kapat

---

## 🌐 Ağ Güvenliği — Wi‑Fi ve Ortak Ağlar
- WPA2/WPA3 şifreli Wi‑Fi kullan
- Modem/Router varsayılan parolalarını değiştir
- Ortak Wi‑Fi’da:
  - Hassas işlemlerden kaçın (mümkünse)
  - HTTPS zorunlu
  - Paylaşımı/Discovery’yi kapat
  - Gerekirse güvenilir VPN kullan

---

## 💾 Yedekleme — 3‑2‑1 Kuralı
- 3 kopya: 1 ana + 2 yedek
- 2 farklı ortam: Bulut + harici disk
- 1 kopya farklı yerde (offline/air‑gap)
- Otomatik yedekleme planı
- Geri yükleme testleri (deneme)

Ransomware’a karşı en etkin kalkan: Sağlam yedek.

---

## 📎 Dosya ve Bağlantı Güvenliği
- Uzantılara dikkat: .exe, .scr, .js, .vbs, .bat
- Ofis dosyalarında makrolara şüpheyle yaklaş
- Sıkıştırılmış dosyalarda (zip/rar) bilinmeyen içerik → açma
- İndirilen dosyaları güvenlik yazılımıyla tara
- Kısa linkleri (bit.ly vb.) önizleme ile doğrula

---

## 🔐 Şifreleme ve Güvenli Paylaşım
- İletişim: Uçtan uca şifreli mesajlaşma tercih edin
- Dosya paylaşım: Şifreli arşiv + ayrı kanaldan parola
- Bulut linkleri: Süreli link, indirme sınırı, sadece görüntüleme
- Hassas veriler: Mümkünse paylaşma; gerekirse minimum veri

---

## 🚨 Olay Anında Ne Yapmalı?
- Şüpheli linke tıkladın/ek indirdin:
  - İnternetten çık, dosyayı sil, tam tarama yap
  - Parolaları değiştir, 2FA’yı güçlendir
- Hesap ele geçirildi:
  - Parola sıfırla, tüm oturumları kapat
  - Bağlı uygulamaları/devre dışı bırak
  - Kurtarma e-postası/telefonu doğrula
- Finansal dolandırıcılık şüphesi:
  - Banka ile iletişime geç, kartı/geçişleri blokla
  - Resmi makamlara başvur

Her adımı not al; gerektiğinde kanıt olarak sakla.

---

## ⌨️ Alışkanlık Kısayolları
- Güncelleme: .kbd[Haftalık] kontrol
- Parola kasası: .kbd[Aylık] denetim/temizlik
- 2FA: .kbd[Hemen] kritik hesaplarda aktif
- Yedekleme: .kbd[Otomatik] + .kbd[Aylık] test
- Paylaşımlar: .kbd[Her gönderim öncesi] gözden geçir

---

## 🧪 Uygulama — 12 Dakika
Görev:
1) Parola Denetimi
- 3 hesap için benzersiz, güçlü parola oluşturun (kasayla)
- Ana parolanız için parola cümlesi yazın (paylaşmayın)

2) 2FA Etkinleştirme
- E‑posta + 2 önemli hesabınızda 2FA açın
- Kurtarma kodlarını güvenle kaydedin

3) Phishing Analizi
- Eğitmen örnek e-postalarını inceleyin: Şüphe işaretlerini listeleyin

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Kontrol Listesi
- [ ] Güçlü ve benzersiz parolalar
- [ ] Parola yöneticisi kurulumu
- [ ] 2FA kritik hesaplarda aktif
- [ ] Cihaz/uygulama güncellemeleri tamam
- [ ] Ortak Wi‑Fi’da güvenlik önlemleri
- [ ] Yedekleme planı ve test
- [ ] Phishing farkındalık kontrolü

---

## 🧰 Kaçınılacaklar ve İpuçları
Kaçınılacaklar:
- Aynı parolayı her yerde kullanmak
- SMS 2FA’yı tek koruma sanmak
- Ortak ağda giriş bilgilerini kaydetmek
- “Herkese açık” paylaşımları kalıcı bırakmak

İpuçları:
- Kritik hesap → Donanım anahtarı (mümkünse)
- Paylaşımlı cihazda → Gizli/Pvt pencere + çıkış
- Sosyal medyada → Kısıtlı görünürlük ve etiketleme izinleri
- Düzenli güvenlik “bakım günü” planlayın

---

## 🧑‍🏫 Kurum/Okul Ortamlarında
- Paylaşımlı cihazlar: Kendi hesabınla giriş yap, işin bitince çıkış
- USB bellek: Bilinmeyen bellekleri takma, önce tara
- Yazılım yükleme: Sadece yetkili/onaylı kaynaklar
- Politikalar: Kabul edilebilir kullanım kurallarına uy

---

## 🔗 Yararlı Kaynaklar
- Google Hesap Güvenliği: https://myaccount.google.com/security
- İki Adımlı Doğrulama Bilgileri:
  - Google: https://support.google.com/accounts/answer/185839
  - Microsoft: https://support.microsoft.com/account-billing/two-step-verification-setup
  - Apple: https://support.apple.com/HT204915
- Parola İpuçları: https://www.ncsc.gov.uk/collection/passwords
- Güvenli İnternet İpuçları: https://www.staysafeonline.org/

Not: Bağlantıları tarayıcıya kendiniz yazarak ziyaret etmeyi tercih edin.

---

## 🧭 Sonraki Adım (Ödev)
- 3 kritik hesapta 2FA’yı kalıcı hale getirin
- Parola kasasına tüm hesaplarınızı taşıyın
- Aylık “Güvenlik Bakım Planı” yazın:
  - Güncelleme, yedekleme, erişim/oturum denetimi
- Sosyal medya gizlilik ayarlarınızı gözden geçirin

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 öğrenci güvenlik bakım planını paylaşır (60 sn)
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve gelişim alanları

::: notes
Somut, uygulanabilir planları öne çıkarın; karmaşık araçlara boğmayın.
:::

---

## ❓ Soru-Cevap
- 2FA ve parola kasası seçimi
- Phishing doğrulama örnekleri
- Yedekleme ve geri yükleme pratikleri
- Cihaz/ağ güvenliği senaryoları

Teşekkürler! Güvende kalmak bir alışkanlık meselesi. 🚀
---
marp: true
title: "ChatGPT — Doğru Prompt Yazma"
description: "GSB Dijital Okuryazarlık Eğitimi — 10. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 10. Ders · ChatGPT"
style: |
  :root {
    --primary: #2F80ED;
    --accent: #F2994A;
    --success: #27AE60;
    --warning: #E2B93B;
    --danger: #EF4444;
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
  .bad { color: var(--danger); font-weight: 700; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: start; }
  ul.tight > li { margin: 6px 0; }
  .kbd { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; background: #F3F4F6; border: 1px solid #E5E7EB; padding: 2px 6px; border-radius: 6px; }
---


<!-- _class: lead -->


# ChatGPT
<div class="lesson-badge"><span class="number">10</span><span class="label">Ders</span></div>


<div class="card" style="margin-top: 12px;">
  <div class="pill">GSB Dijital Okuryazarlık</div>
  <h2 style="margin: 10px 0 4px;">Doğru Prompt Yazma</h2>
  <p style="margin: 0; color: #374151;">10. Ders · Süre: 60 dk · Seviye: Başlangıç–Orta · Uygulamalı</p>
</div>
## Doğru Prompt Yazma

GSB Dijital Okuryazarlık — 10. Ders

- Süre: 60 dakika
- Seviye: Başlangıç–Orta
- Format: Uygulamalı

::: notes
Hedef: Her katılımcı “rol, bağlam, görev, kısıt, biçim ve değerlendirme” içeren etkili prompt’lar yazmayı pratik edecek.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- ChatGPT’nin güçlü ve zayıf yanlarını temel seviyede açıklayabileceksiniz.
- Etkili prompt iskeletini (rol + bağlam + görev + biçim + kısıt + örnek) uygulayabileceksiniz.
- Çıktıyı tekrar prompt’ları ile iyileştirebileceksiniz.
- Güvenli/etik kullanım ve doğrulama adımlarını bileceksiniz.
- Farklı kullanım senaryoları için şablon prompt’lar oluşturabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş: ChatGPT nedir? Nerede yararlıdır?
- 15 dk — Prompt iskeleti ve iyi/kötü örnekler
- 15 dk — Uygulama: Taslak → İyileştirme tekrarları
- 10 dk — Güvenli ve etik kullanım, doğrulama
- 10 dk — Mini vitrin, kaynaklar, soru-cevap

---

## 🧭 ChatGPT Nedir?
- Büyük dil modeli tabanlı bir metin üretim asistanı
- Güçlü yanlar: Özet, yeniden yazım, fikir üretimi, örnekleme, biçimlendirme
- Sınırlılıklar: Yanılsama (uydurma), güncel bilgi eksiği, hesap ve doğruluk sorunları
- Kural: Kritik kararlar için her zaman insan denetimi + kaynak doğrulama

> “İyi bir çıktı, iyi bir prompt ile başlar.”

---

## 🧱 Etkili Prompt İskeleti
1) Rol: “Deneyimli … gibi davran”
2) Bağlam: “Hedef kitle: 10. sınıf; konu: …”
3) Görev: “Özetle / Açıkla / Plan yap / Dönüştür”
4) Biçim: “Madde madde / tablo / başlıklarla”
5) Kısıtlar: “En fazla 150 kelime, jargon minimum”
6) Örnek: “Örnek bir madde: …”
7) Değerlendirme: “Sonunda kontrol listesine göre değerlendir”

---

## 🧪 Kötü → İyi Prompt Örneği
Kötü:
- “Enerji tasarrufunu açıkla.”

Daha iyi:
- “Sen bir fen bilimleri öğretmenisin. Lise 9. sınıf seviyesinde enerji tasarrufunu 5 maddede açıkla. Jargonu minimum tut. Her maddeye 1 somut örnek ekle. Toplam 120–150 kelime.”

İyileştirme:
- “Şimdi 3 pratik öneriyi tablo formatında ekle (Öneri | Tahmini Etki | Zorluk).”

---

## 🔁 Döngüsel İyileştirme (Iterative Prompting)
- “Kısalt ve daha anlaşılır yap.”
- “2 alternatif başlık öner.”
- “Hataları bul ve düzelt.”
- “Kod/Metin’i ‘adım adım açıklama’ ile açıkla.”
- “Aynı içeriği 14–16 yaş için sadeleştir.”

İpucu: Sonuçları görünce prompt’u revize etmeye hazır olun.

---

## 🧰 Hazır Prompt Şablonları (Genel)
Özet çıkarma:
- “X metnini 5 maddeyle özetle; her madde max 20 kelime, jargon minimum.”

Yeniden yazım:
- “Metni 9. sınıf seviyesine göre kısalt ve sadeleştir; önemli terimleri parantez içinde açıkla.”

Biçim dönüştürme:
- “Metni tabloya dönüştür (Kavram | Kısa Tanım | Örnek).”

---

## 🧰 Şablonlar (Eğitim)
Konu anlatımı:
- “Sen biyoloji öğretmenisin. [Konu] için 10. sınıf seviyesinde kısa ders notu yaz. Başlıklar: Tanım, Neden önemli, Örnekler, Mini-Quiz (3 soru).”

Soru üretimi:
- “[Konu] için 3 kolay, 2 orta, 1 zor çoktan seçmeli soru üret. Doğru cevapları en sonda ayrı listele.”

Geri bildirim:
- “Bu paragrafı değerlendir: Netlik, Örgü, Dil bilgisi, Örnekler. Her başlık için 10 üzerinden puan ve öneri ver.”

---

## 🧰 Şablonlar (Yazma ve İçerik)
E-posta taslağı:
- “Profesyonel, kısa ve net bir e-posta yaz. Amaç: [Amaç]. Üslup: Nazik ve çözüm odaklı. Biçim: Selam, 3 madde, kapanış.”

Blog giriş yazısı:
- “Bu notlardan 150 kelimelik bir blog girişi yaz: [notlar]. Ton: Bilgilendirici ve akıcı.”

Başlık fikirleri:
- “[Konu] için 10 yaratıcı başlık öner. Her başlık 50 karakteri geçmesin.”

---

## 🧰 Şablonlar (Kod ve Teknik)
Kod açıklama:
- “Aşağıdaki kodu satır satır açıkla ve olası hataları belirt. Sonunda iyileştirme önerilerini ver. [kod]”

Regex üretimi:
- “Şu kuralı yakalayacak bir regex yaz ve örneklerle test et: [kural]. Ardından sınır durumlarını listele.”

Veri dönüşümü:
- “Bu CSV’yi JSON’a dönüştür ve şema çıkar. [örnek-CSV]”

Not: Kritik sistemlerde sonuçları mutlaka test edin.

---

## 🧠 İpuçları
- Net hedef → net çıktı
- Kitleyi, amacı ve kapsamı belirtin
- Sınırlandırın (kelime sayısı, madde sayısı, biçim)
- Gerekirse örnek verin; “Böyle değil, böyle”
- Karşılaştırma isteyin (Seçenek A vs B)
- “Önce sorunları bul, sonra düzelt” gibi iki aşamalı görevler verin

---

## 🧯 Sınırlılıklar ve Riskler
- Yanılsama: Güvenle söylediği yanlışlar
- Kaynak: Verdiği linkler/atıflar hatalı olabilir
- Güncellik: Bazı bilgiler eski olabilir
- Gizlilik: Kişisel/sensitif veri paylaşmayın
- Telif/etik: Atıf kurallarına uyun; özgünlük sorumludur

Kural: Önemli çıktıları çapraz doğrulayın.

---

## 🛡️ Güvenli ve Etik Kullanım
- Kişisel verileri (TC, adres, özel bilgiler) yazmayın
- Hassas/veriye dayalı iddialar için kaynak isteyin ve kontrol edin
- “Yardımcı” olarak kullanın; öğrenme yerine geçmesin
- Üretimi sahiplenmeden önce gözden geçirin ve düzenleyin
- Şeffaflık: Gerekirse YZ’den yararlandığınızı belirtin

---

## 📐 Çıktı Biçimlendirme Teknikleri
- “MD tablo formatında yaz.”
- “Başlıklar: H2, alt başlıklar: H3.”
- “Her maddenin başına emoji ekle (maks. 1).”
- “Önce özet, sonra detay.”
- “En sonda 3 maddelik eylem listesi ver.”

İpucu: Biçim talimatlarını prompt sonunda özetleyin.

---

## ⌨️ Yararlı “Prompt Operatörleri”
- “Rol yap”: “Sen … gibi davran”
- “Kısıt”: “En fazla … kelime”
- “Biçim”: “Tablo”, “madde”, “başlık”, “JSON”
- “Dil”: “Türkçe yaz”, “B1 düzeyi”
- “Ton”: “Resmi / samimi / ikna edici”
- “Adım adım”: “Önce hataları bul, sonra düzelt”

Not: Aynı işi farklı kelimelerle deneyin, kıyaslayın.

---

## 🧪 Uygulama — 12 Dakika
Görev:
1) Taslak Prompt
- Bir konuyu seçin ve iskelete göre ilk prompt’u yazın (rol+bağlam+görev+biçim+kısıt).

2) İyileştirme
- Çıktıyı görün → “kısalt”, “sadeleştir”, “tabloya dönüştür”, “2 alternatif başlık” gibi tekrarlarla geliştirin.

3) Doğrulama
- “Varsa hata/eksik var mı? 3 maddede düzeltme öner.” isteyin.

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Değerlendirme Kontrol Listesi
- [ ] Rol/bağlam/görev net
- [ ] Biçim ve kısıtlar tanımlı
- [ ] Döngüsel iyileştirme uygulandı
- [ ] Güvenli/etik kullanım ilkelerine uyuldu
- [ ] Çapraz doğrulama yapıldı
- [ ] Nihai çıktı hedef kitleye uygun

---

## 🧰 Kaçınılacaklar ve İpuçları
Kaçınılacaklar:
- Belirsiz ve tek cümlelik prompt’lar
- Kişisel/sensitif veri paylaşımı
- Kaynaksız “kesin doğru” varsayımı
- “Kopyala-yapıştır” ve bitti yaklaşımı

İpuçları:
- İterasyon: “Geliştir, kısalt, biçimlendir, test et”
- Karşılaştırma: “A ve B’yi kıyasla, karar kriterlerinden puanla”
- Kapsam: “Bu çıktı kime, hangi amaçla?”

---

## 🧩 Mini Şablon Kütüphanesi
- “Özetle (madde madde, 120 kelime, B1 dil).”
- “Kısa sunum planı oluştur (5 slayt, başlık+2 nokta).”
- “Metni tabloya dönüştür (Kavram|Tanım|Örnek).”
- “3 quiz sorusu üret (2 kolay, 1 orta).”
- “Aynı metni 14–16 yaş için sadeleştir.”
- “Hataları bul ve düzelt, her düzeltmeye kısa gerekçe yaz.”

Kendi şablonlarınızı sınıfla paylaşın.

---

## 🔗 Yararlı Kaynaklar
- “Prompt Engineering” rehberleri (çeşitli çevrimiçi kaynaklar)
- Etik YZ kullanım kılavuzları
- Yazım/biçim kontrol araçları
- Akademik doğrulama ve kaynak arama yöntemleri

Not: Güncel ve resmi kaynakları tercih edin.

---

## 🧭 Sonraki Adım (Ödev)
- Seçtiğiniz bir konu için:
  - 1 sayfa özet (B1 seviye, max 200 kelime)
  - 5 slayt taslağı (başlık + 2 madde)
  - 3 quiz sorusu (yanıtlar en sonda)
- Kullanılan prompt’ları ekleyin (şeffaflık)
- Çapraz doğrulama notu: “Doğruladığım kaynaklar…”

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 öğrenci geliştirilmiş prompt’larını ve çıktılarını paylaşır
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve geliştirme alanları

::: notes
Zamanı planlı tutun, iyi örnekleri görünür kılın.
:::

---


## ❓ Soru-Cevap

- Prompt iskeleti ve varyasyonları

- Döngüsel iyileştirme stratejileri

- Güvenli/etik kullanım senaryoları

- Doğrulama ve kaynak yönetimi



Teşekkürler! Etkili prompt’larla üretkenliğiniz katlanacak. 🚀

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
Bu slaytı, güçlü bir görsel hikaye ve kısa bir mesajla kullanın (maks. 1 satır).
</div>

---
## 💡 İkonlu İpuçları

- 🎯 Net hedef: Kullanım amacını ve hedef kitleni baştan belirle
- 🧭 Yapı: Başlık hiyerarşisi + az metin, örnek ve görsel ağırlık
- ✅ Tutarlılık: En fazla 2 font, uyumlu renk paleti
- 🔍 Doğrulama: Kritik çıktılarda birincil kaynaklarla çapraz kontrol
- 🔒 Gizlilik: Kişisel/sensitif verileri modele yazmaktan kaçın
- ♿ Erişilebilirlik: Yeterli kontrast ve okunur font boyutu

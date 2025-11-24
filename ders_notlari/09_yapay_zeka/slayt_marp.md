---
marp: true
title: "Yapay Zeka — Temeller ve Uygulamalar"
description: "GSB Dijital Okuryazarlık Eğitimi — 9. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 9. Ders · Yapay Zeka"
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
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start; }
  ul.tight > li { margin: 6px 0; }
  .kbd { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; background: #F3F4F6; border: 1px solid #E5E7EB; padding: 2px 6px; border-radius: 6px; }
---



# Yapay Zeka

<div class="lesson-badge"><span class="number">9</span><span class="label">Ders</span></div>
<div class="card" style="margin-top: 12px;">

  <div class="pill">GSB Dijital Okuryazarlık</div>
  <h2 style="margin: 10px 0 4px;">Temeller ve Uygulamalar</h2>
  <p style="margin: 0; color: #374151;">9. Ders · Süre: 60 dk · Seviye: Başlangıç · Uygulamalı</p>
</div>
## Temeller ve Uygulamalar

GSB Dijital Okuryazarlık — 9. Ders


- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Hedefleri paylaşın: Herkes dersten “Yapay Zekayı günlük hayatında güvenli ve verimli kullanma” becerisiyle çıkacak.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Yapay zeka (YZ), makine öğrenmesi (MÖ) ve derin öğrenme (DÖ) arasındaki farkları açıklayabileceksiniz.
- Generatif YZ ve büyük dil modellerinin (LLM) nasıl çalıştığını temel seviyede anlayacaksınız.
- Temel prompt (komut) yazım tekniklerini uygulayabileceksiniz.
- YZ’nin sınırlamaları, etik ve güvenlik risklerini tanıyacaksınız.
- Günlük yaşam ve eğitimde YZ’den güvenli ve verimli yararlanabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş: YZ nedir ve nerede karşımıza çıkar?
- 15 dk — Temeller: MÖ/DÖ/LLM kavramları, generatif YZ
- 15 dk — Uygulama: Prompt yazma ve sonuç iyileştirme
- 10 dk — Etik, gizlilik, önyargı ve doğrulama
- 10 dk — Mini vitrin, kaynaklar, soru-cevap

---

## 🧭 Neden Yapay Zeka?
- Her gün: Arama motorları, öneri sistemleri, yazım denetimi, çeviri
- Eğitim: Özet çıkarma, kavram açıklama, pratik soru üretme
- Üretkenlik: Taslak metin, e-posta, fikir üretme, kod tamamlama
- Yaratıcılık: Görsel/video üretimi, müzik, hikaye taslağı

> “YZ; insanı ikame etmekten çok, insanı güçlendirmek için bir araçtır.”

---

## 🤖 Temel Tanımlar
- Yapay Zeka (AI): Bilgisayarların “zeki” davranışlar sergilemesi
- Makine Öğrenmesi (ML): Veriden öğrenen algoritmalar
- Derin Öğrenme (DL): Çok katmanlı yapay sinir ağları
- Generatif YZ: Yeni içerik üreten modeller (metin, görsel, ses)
- Büyük Dil Modelleri (LLM): Çok geniş metinle eğitilen dil modelleri

Basit ayrım: Veri → Model → Tahmin/Üretim

---

## 🧠 ML Türleri — Kısa Bakış
- Denetimli Öğrenme: Etiketli veri ile (Sınıflandırma, Regresyon)
  - Örn: E-posta “spam mı değil mi?”
- Denetimsiz Öğrenme: Etiket yok, kalıp keşfi (Kümeleme, Boyut indirgeme)
  - Örn: Benzer belgelere otomatik gruplama
- Pekiştirmeli Öğrenme: Deneme-yanılma ve ödül
  - Örn: Oyun oynayan ajan, robot kontrolü

---

## ✨ Generatif YZ ve LLM’ler
- Transformer mimarisi → Dikkat (Attention) mekanizması
- LLM çalışma fikri: “Sıradaki en olası kelime”
- Güçlü yanlar:
  - Dil içi örüntüleri yakalama, hızlı taslak üretimi
- Sınırlılıklar:
  - Yanılsama (uydurma), hesaplama hataları, güncel bilgi eksiği

Not: LLM’ler “bilmez”; istatistiksel tahmin yapar.

---

## 🧪 Uygulama — Prompt Temelleri
İyi bir prompt genelde şu unsurları içerir:
- Rol: “Sen deneyimli bir öğretmensin…”
- Bağlam: “Lise 10. sınıf düzeyi, konu: fotosentez…”
- Görev: “Kısa bir özet yaz.”
- Biçim: “Madde madde, max 5 madde.”
- Kısıt: “Teknik jargon minimum, 120–150 kelime.”
- Örnek: “Örnek bir madde: …”
- Değerlendirme: “Cevabı kontrol listesine göre gözden geçir.”

---

## 🧪 Uygulama — Prompt Örneği
Amaç: Bir konuyu hızlıca kavramak

Kötü:
- “Fotosentezi açıkla.”

Daha iyi:
- “Sen biyoloji öğretmenisin. Lise 10. sınıf seviyesinde fotosentezi 5 maddeyle açıkla. Jargonu minimum tut. Son maddede günlük hayatla bağlantı kur. 120–150 kelimeyi aşma.”

İyileştirme:
- “Şimdi 3 çoktan seçmeli pratik soru ekle ve doğru yanıtları sonunda ayrı listele.”

---

## 🧩 Prompt İyileştirme İpuçları
- Adım adım: “Önce geri planı özetle, sonra örnekle açıkla.”
- Sınırlandırma: “Cevabı 8 maddeyle sınırla.”
- Biçim: “Tablo formatında sun.”
- Düşünme yönlendirme: “Önce kriterleri değerlendir, sonra karar ver.”
- Doğrulama: “Kaynak varsa belirt; yoksa ‘bilinmiyor’ de.”
- Tekrar: “1. denemeyi kısaltarak yeniden yaz.”

---

## 🧯 Sınırlamalar ve Riskler
- Halüsinasyon: Yanlış ama “inandırıcı” cevaplar
- Önyargı: Eğitim verisindeki taraflılık
- Gizlilik: Hassas verilerin modele verilmesi
- Telif: İçerik üretiminde hak ve atıf sorunları
- Güncellik: Modelin bilgi kesim tarihi

Kural: Kritik kararları YZ’ye bırakmayın; insan denetimi şart.

---

## 🛡️ Güvenli ve Sorumlu Kullanım
- Kişisel/sensitif veri paylaşmayın
- Hassas konularda birincil kaynak doğrulaması yapın
- Telif ve atıf kurallarına uyun
- Eğitimde: Yardımcı araç, emek ikamesi değil
- Şeffaflık: YZ’den yararlandığınızı belirtin

---

## 📚 Eğitimde Kullanım Senaryoları
- Özet çıkarma, kelime hazinesi geliştirme
- Alternatif açıklamalarla “farklı anlatım” sağlama
- Pratik soru üretme/çözüm denetimi
- Metni sadeleştirme/yerelleştirme
- Fikir üretimi: Proje konusu, iskelet çıkarma
- Kod yardımı: Basit örnek ve hata ayıklama

---

## 🧪 Atölye — 12 Dakika
Görev 1 — Konu Özeti:
- Seçilen bir ders konusunu (örn. İklim değişikliği) “hedef kitle ve kapsam” belirterek 5 maddede özetletin.

Görev 2 — Soru Üret:
- Aynı konu için 3 çoktan seçmeli, 2 açık uçlu soru isteyin; doğru yanıtları en sona koydurun.

Görev 3 — Mini Plan:
- 5 slaytlık sınıf içi mini sunum taslağı isteyin (başlıklar, kısa notlar).

---

## 🧪 Mini Proje (Ödev)
- “YZ Destekli Mini Rehber”
  - Konu: Seçtiğin bir ders teması (örn. Yenilenebilir enerji)
  - Teslim: 1 sayfa özet + 5 slayt taslağı + 3 quiz sorusu
  - Kısıtlar:
    - Hedef kitle: 14–16 yaş
    - Jargon minimum, örnek odaklı
    - Kaynak/atıf varsa belirt
  - Not: YZ’ye verdiğin prompt’ları dosyaya ekle (şeffaflık)

---

## ✅ Değerlendirme Kontrol Listesi
- [ ] YZ/MÖ/DÖ/LLM farklarını açıklayabiliyor
- [ ] Etkili prompt yazımı (rol, bağlam, görev, biçim, kısıt)
- [ ] Çıktıyı doğrulama ve düzeltme uygulandı
- [ ] Etik/gizlilik/telif risklerini biliyor
- [ ] Mini proje çıktılarını sundu

---

## 🧰 Kaçınılacaklar ve İpuçları
Kaçınılacaklar:
- “Tek cümlelik” belirsiz prompt’lar
- Kaynaksız “kesin doğru” varsayımı
- Kişisel/veri paylaşımı
- YZ çıktısını “kopyala-yapıştır” ve bitti yaklaşımı

İpuçları:
- Yineleme: “Geliştir/yeniden yaz/kısalt/uzat”
- Karşılaştırma: “Seçenek A ve B’yi kıyasla”
- Biçim: “Çıktıyı tablo/madde/başlıklarla ver”

---

## 🔗 Yararlı Kaynaklar
- “Elements of AI” — Ücretsiz giriş dersi
- “Google AI Education” — Temel kavramlar
- “Fast.ai” — Uygulamalı materyaller
- “DeepLearning.AI” — Kısa kurslar
- “Responsible AI” — Etik ve güvenli kullanım rehberleri

Not: Kaynakları her zaman güncel ve resmi sitelerden kontrol edin.

---

## 🧭 Sonraki Ders (Önizleme)
- 10. Ders: ChatGPT — Doğru Prompt Yazma
  - Prompt kalıpları
  - Gelişmiş teknikler
  - Çıktı denetimi ve tekrar iyileştirme

Hazırlık: Bugünkü mini projede yazdığınız prompt’ları saklayın.

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 öğrenci mini çıktısını (özet + 1 slayt + 1 soru) paylaşır
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve geliştirme alanları

::: notes
Zamanı planlı tutun; iyi örnekleri görünür kılın.
:::

---


## ❓ Soru-Cevap

- Teknik sınırlamalar ve doğrulama

- Etik ve güvenlik senaryoları

- Eğitimde pratik kullanım

- Prompt iyileştirme püf noktaları



Teşekkürler! YZ ile üretken ve sorumlu bir yolculuğa hazırsınız. 🚀

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
- 🧭 Yapı: Başlık hiyerarşisi + az metin, çok örnek ve görsel
- ✅ Tutarlılık: En fazla 2 font, sınırlı ve uyumlu bir renk paleti
- 🔍 Doğrulama: Kritik iddialarda her zaman birincil kaynaklarla çapraz kontrol
- 🔒 Gizlilik: Kişisel/sensitif verileri modele yazmaktan kaçın
- ♿ Erişilebilirlik: Yeterli kontrast ve okunur font boyutu

---
marp: true
title: "Trello — Dijital Planlama ve Proje Yönetimi"
description: "GSB Dijital Okuryazarlık Eğitimi — 5. Ders"
theme: default
paginate: true
size: 16:9
footer: "GSB Dijital Okuryazarlık Eğitimi · 5. Ders · Trello"
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

# Trello
<div class="card" style="margin-top: 12px;">
  <div class="pill">GSB Dijital Okuryazarlık</div>
  <h2 style="margin: 10px 0 4px;">Dijital Planlama ve Proje Yönetimi</h2>
  <p style="margin: 0; color: #374151;">5. Ders · Süre: 60 dk · Seviye: Başlangıç · Uygulamalı</p>
</div>

## Dijital Planlama ve Proje Yönetimi
GSB Dijital Okuryazarlık — 5. Ders

- Süre: 60 dakika
- Seviye: Başlangıç
- Format: Uygulamalı

::: notes
Bu derste herkes bir proje panosu kuracak, kart akışıyla temel Kanban pratiği yapacak ve mini otomasyon kuralı deneyecek.
:::

---

## 🎯 Öğrenme Hedefleri
Bu dersin sonunda:
- Kanban yaklaşımını ve Trello’nun temel kavramlarını açıklayabileceksiniz.
- Pano, liste ve kart yapılarıyla proje akışı kurabileceksiniz.
- Etiket, üye, son tarih, checklist ve ek dosyalarla işi organize edebileceksiniz.
- Filtreleme, arama ve Power-Up’larla verimi artırabileceksiniz.
- Butler ile basit otomasyon kuralı oluşturabileceksiniz.

---

## ⏱️ Akış ve Zaman Planı
- 10 dk — Giriş: Trello ve Kanban
- 15 dk — Arayüz turu ve temel kavramlar
- 15 dk — Uygulama: Pano kurulumu ve kart akışı
- 10 dk — Otomasyon ve Power-Up örnekleri
- 10 dk — Paylaşım, kısayollar ve mini vitrin

---

## 🧭 Neden Trello?
- Görsel ve basit proje takibi (Kanban)
- Ekip ile gerçek zamanlı işbirliği
- Sürükle-bırak akışı, düşük öğrenme eğrisi
- Power-Up’lar ile esnek genişleme
- Ücretsiz planla başlamak kolay

> “Görselleştirilen iş, yönetilebilir olur.”

---

## 🚪 Başlangıç: Erişim
- trello.com → Ücretsiz hesap oluşturun
- Workspace oluşturun (sınıf/grup bazlı)
- “Create board” → Proje panosu açın
- Görünürlük: Private / Workspace / Public (öneri: Private/Workspace)

İpucu: Pano adı kısa ve açıklayıcı olsun (örn. “GSB_Proje_Takibi”).

---

## 🖥️ Arayüz Turu
- Üst: Pano adı, görünürlük, Power-Up, Otomasyon, Menü
- Orta: Listeler (kolonlar) ve kartlar
- Kart: Başlık, açıklama, etiketler, üyeler, son tarih, checklist, ekler, kapak
- Menü: Arka plan, etkinlik kaydı, pano ayarları

İlk adım: Listeleri kurun (To Do / Doing / Done).

---

## 🧩 Kanban Mantığı (Kısa)
- İş akışını görselleştir: “Yapılacak → Yapılıyor → Bitti”
- WIP (Work in Progress) limiti: Aynı anda az iş
- Sürekli akış: Kartlar soldan sağa hareket eder
- Hızlı geri bildirim ve darboğaz tespiti

Amaç: Şeffaflık, odak ve akış.

---

## 🗂️ Pano Yapısı Önerisi
Örnek Listeler:
- Backlog (fikirler/toplanacak işler)
- To Do (seçilen işler)
- Doing (devam edenler)
- Review (kontrol/geri bildirim)
- Done (tamamlananlar)

İpucu: Pano açıklamasına kuralları yazın (örn. “Kart taşıyan kişi üye olsun”).

---

## 🃏 Kart Temelleri
Kart özellikleri:
- Başlık ve Açıklama
- Üyeler (sorumlular)
- Etiketler (renk/kategori)
- Son tarih (due date) ve hatırlatıcı
- Checklist (adım adım görevler)
- Ek dosyalar (Drive/PC)
- Kapak (renk/görsel)

Kart yaşam döngüsü: Oluştur → Zenginleştir → Taşı → Tamamla/Arşivle.

---

## 🏷️ Etiket ve Filtreleme
- Etiket renkleriyle kategorize edin (örn. Tasarım, Araştırma, Acil)
- Arama/filtre: Üstte “Filter” → Etiket/üye/tarih ile daraltın
- Hızlı görünürlük: Tahmin edilmesi kolay renkler seçin

İpucu: Etiket isimlerini standartlaştırın (örn. “Acil”, “Öncelik-1”).

---

## ✅ Checklist ve Şablon Kartlar
- Büyük görev → alt adımlar için checklist
- Yüzde ilerleme otomatik hesaplanır
- Şablon kart: “Make template” ile tekrarlanabilir görev iskeleti
- Örnek: “Sosyal Medya Postu” şablonu (Metin, görsel, onay)

Kural: Tekrarlayan işler için şablon kullanın.

---

## ⏰ Son Tarih, Takvim ve Görünümler
- Due date + hatırlatıcı = zaman yönetimi
- Calendar Power-Up ile takvim görünümü
- Timeline/Table/Calendar gibi farklı görünümler (plan türüne bağlı)
- Kartları tarih aralığına göre planlayın

Not: Ücretsiz planda sınırlı Power-Up kullanılabilir.

---

## 🔌 Power-Up Örnekleri
- Calendar: Son tarihleri takvimde görün
- Google Drive: Dosyaları doğrudan bağlayın
- Slack/Teams: Bildirim entegrasyonu
- Custom Fields: Özel alanlar (puan, link, seçim)

İpucu: “Az ama öz” Power-Up verimi artırır.

---

## 🤖 Butler Otomasyon (Giriş)
- Kural: “Eğer … ise … yap” mantığı
- Örnek kural:
  - “Kart ‘Doing’e taşındığında → etiketi ‘Devam’ ekle ve due date +3 gün ata”
- Butonlar: Liste/kart butonlarıyla hızlı işlemler
- Zamanlanmış tetikleyiciler: Günlük/haftalık görevler

Dikkat: Küçük otomasyonlar bile büyük fark yaratır.

---

## 👥 İşbirliği ve İletişim
- Üyeler: Kart sorumluları
- Yorumlar: Tartışma, karar ve notlar
- @mention: Kişi etiketleme
- Ekler: Örnekler, dosyalar
- Bildirimler: Takip edilen kart/liste/pano

İpucu: Kararları kart yorumunda sabitleyin (pin).

---

## ⌨️ Yararlı Kısayollar
- Kart ekle: .kbd[N] (listede iken)
- Kartı düzenle: .kbd[E]
- Pano arama: .kbd[/]
- Kartı taşı: .kbd[,] ve .kbd[.]
- Etiket kısayolları: .kbd[1–9]
- Hızlı aç: Kart üzerine .kbd[Enter]

Not: Kısayolları Help → Shortcuts ekranından keşfedin.

---

## 🧪 Uygulama — 12 Dakika
Görev:
- “GSB_Ekip_Projesi” panosu oluşturun
- Listeler: Backlog / To Do / Doing / Review / Done
- En az 6 kart: Başlık + açıklama + etiket + üye
- 2 kartta checklist + due date
- 1 basit Butler kuralı (örn. Done’a taşınan kart arşivlensin)

Mentor turu: Soruları yerinde yanıtlayacağız.

---

## ✅ Değerlendirme Kontrol Listesi
- [ ] Pano ve listeler kuruldu
- [ ] 6+ kart eklendi ve zenginleştirildi
- [ ] Etiket/üye/tarih kullanıldı
- [ ] Checklist ve ek dosyalar eklendi
- [ ] En az 1 otomasyon kuralı tanımlandı
- [ ] Filtreleme ve arama denendi
- [ ] Pano paylaşıldı (ekip üyeleri davetli)

---

## 🧱 Örnek Pano İskeleti
- Backlog
  - Fikir Toplama
  - Kaynak Listesi (linkler)
- To Do
  - Haftalık görevler
- Doing
  - Aktif kartlar (her kartta sorumlu + due)
- Review
  - Kontrol/geri bildirim gerekenler
- Done
  - Tamamlananlar (aylık arşiv)

İpucu: “Done (2024-11)” şeklinde aylık arşiv listesi açın.

---

## 🧰 Kaçınılacaklar ve İpuçları
- Kaçınılacaklar:
  - Karmaşık, çok fazla liste
  - Labelsiz/üy esiz kartlar
  - Güncellenmeyen son tarihler
- İpuçları:
  - Haftalık gözden geçirme (5 dk)
  - WIP limiti (Doing max 3)
  - Şablon kartlar ile standartlaştırma

---

## 🔗 Yararlı Kaynaklar
- Trello Başlangıç Rehberi: https://trello.com/guide
- Kısayollar: https://trello.com/shortcuts
- Butler Otomasyon: https://trello.com/butler
- Power-Up Galerisi: https://trello.com/power-ups

---

## 🧭 Sonraki Adım (Ödev)
- Pano şablonu oluşturun ve ekibinizle paylaşın
- 1 “tekrarlayan” otomasyon kuralı ekleyin (haftalık)
- 3 kartı “tamamlanma” akışından geçirin (To Do → Done)
- Kısa bir not: Neyi iyileştirirdiniz?

---

## 🌟 Mini Vitrin — 6 Dakika
- 3 ekip panosunu hızlı tur
- Akran geri bildirimi: 1 güçlü yön, 1 öneri
- Eğitmen notları ve sonraki adımlar

::: notes
Zamanı planlı tutun ve iyi örnekleri görünür kılın.
:::

---


## ❓ Soru-Cevap

- Pano tasarımı ve akış

- Butler kural senaryoları

- Power-Up seçimleri

- Ekip kullanım pratikleri



Teşekkürler! Düzenli akış ve net sorumluluklarla güçlü takımlar kurmaya hazırsınız. 🚀

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
Bu slaytı, pano akışını anlatan kısa bir mesaj ve tek cümlelik ana fikirle kullanın.
</div>

---

## 💡 İkonlu İpuçları

- 🧭 Akış: To Do → Doing → Review → Done dizilimini basit tut
- 🔖 Etiketler: Az ve anlamlı label paleti kullan, ekipte standartlaştır
- ⛳ WIP limiti: Doing listesindeki iş sayısını sınırlayarak odağı koru
- ☑️ Checklist: Adımları görünür kıl; ilerleme yüzdesini takip et
- ⏰ Due date: Son tarih + hatırlatıcı ile zaman yönetimini netleştir
- 🤖 Butler: Küçük otomasyon kurallarıyla tekrarlı işleri azalt

# Katkıda Bulunma Rehberi 🤝

GSB Dijital Okuryazarlık Eğitimi projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu rehber, projeye nasıl katkı sağlayabileceğinizi açıklamaktadır.

## 📋 İçindekiler
- [Katkı Türleri](#katkı-türleri)
- [Nasıl Başlarım?](#nasıl-başlarım)
- [Pull Request Süreci](#pull-request-süreci)
- [Kod ve İçerik Standartları](#kod-ve-içerik-standartları)
- [Issue Raporlama](#issue-raporlama)
- [Community Guidelines](#community-guidelines)

## 🎯 Katkı Türleri

### 📚 Eğitim İçeriği
- Yeni ders planları ekleme
- Mevcut dersleri güncelleme
- Pratik proje örnekleri geliştirme
- Değerlendirme kriterleri iyileştirme

### 🔧 Teknik İyileştirmeler
- Dokümantasyon düzeltmeleri
- Broken link'leri düzeltme
- Markdown formatı iyileştirmeleri
- Klasör organizasyonu optimize etme

### 🌍 Yerelleştirme
- Farklı dillere çeviri
- Kültürel uyarlamalar
- Bölgesel ihtiyaçlara göre özelleştirme

### 🐛 Hata Raporları
- Yazım hatalarını bildirme
- İçerik hatalarını tespit etme
- Broken resource link'leri raporlama

## 🚀 Nasıl Başlarım?

### 1. Repository'yi Fork Edin
```bash
# GitHub web interface üzerinden "Fork" butonuna tıklayın
# Kendi hesabınıza kopyalanacak
```

### 2. Local'e Clone Edin
```bash
git clone https://github.com/[username]/dijital_okuryazarlik_egitim_gsb.git
cd dijital_okuryazarlik_egitim_gsb
```

### 3. Development Branch Oluşturun
```bash
git checkout -b feature/yeni-ozellik-adi
# veya
git checkout -b fix/duzeltme-adi
# veya
git checkout -b docs/dokumantasyon-adi
```

### 4. Değişikliklerinizi Yapın
- Dosyaları düzenleyin
- Yeni içerik ekleyin
- Test edin ve kontrol edin

### 5. Commit ve Push
```bash
git add .
git commit -m "feat: yeni özellik eklendi

- Detaylı açıklama
- Ne değiştirildi
- Neden değiştirildi"

git push origin feature/yeni-ozellik-adi
```

### 6. Pull Request Açın
- GitHub'da Pull Request oluşturun
- Detaylı açıklama yazın
- Reviewer'ları bekleyin

## 📝 Pull Request Süreci

### PR Checklist
- [ ] Branch adı anlamlı (feat/, fix/, docs/ prefix)
- [ ] Commit mesajları açıklayıcı
- [ ] Değişiklikler test edildi
- [ ] Dokümantasyon güncellendi (gerekiyorsa)
- [ ] Broken link yok
- [ ] Markdown formatı doğru

### PR Şablonu
```markdown
## 📋 Değişiklik Özeti
Kısaca ne değiştirildi:

## 🎯 Motivasyon ve Bağlam
Neden bu değişiklik gerekli:

## 📸 Screenshots (eğer UI değişikliği varsa)
Önce/sonra görselleri:

## ✅ Test Edildi
- [ ] Tüm linkler çalışıyor
- [ ] Markdown düzgün render ediliyor
- [ ] İçerik tutarlı

## 📚 İlgili Issue'lar
Fixes #issue_number
```

## 🎨 Kod ve İçerik Standartları

### Markdown Kuralları
```markdown
# Başlık seviye 1 (sadece ana başlıklar için)
## Başlık seviye 2 (bölüm başlıkları)
### Başlık seviye 3 (alt başlıklar)

- Liste öğeleri tutarlı tire ile
- **Kalın** ve *italik* uygun yerde kullanın
- `Kod` backtick ile
- [Link metni](URL) formatı
```

### Dosya Isimlendirme
```
ders_plani.md        ✅ Doğru (snake_case)
Ders Planı.md       ❌ Yanlış (boşluk)
dersPlanı.md        ❌ Yanlış (camelCase)
```

### İçerik Yapısı
- Her ders planı aynı template'i izlemeli
- Süre belirtilmeli (⏰)
- Hedef belirtilmeli (🎯)
- Pratik projeler bulunmalı (📝)
- Değerlendirme kriterleri olmalı (📊)

### Emoji Kullanımı
```
🎯 Hedef/Amaç
📋 Liste/İçerik
⏰ Süre/Zaman
📝 Pratik/Ödev
💡 İpucu
🔗 Link/Kaynak
📊 Değerlendirme
✅ Başarı/Tamamlandı
❌ Hata/Yanlış
⚠️ Uyarı
```

## 🐛 Issue Raporlama

### Issue Türleri
- **Bug Report**: Hata bildirimi
- **Feature Request**: Yeni özellik önerisi  
- **Documentation**: Dokümantasyon iyileştirmesi
- **Question**: Soru/yardım

### Bug Report Template
```markdown
## 🐛 Hata Açıklaması
Hatanın kısa açıklaması

## 🔍 Hata Adımları
1. Şu sayfaya git
2. Şu linke tıkla
3. Şu hatayı gör

## ✅ Beklenen Davranış
Ne olması gerekiyordu

## 📸 Screenshots
Varsa hata görselleri

## 💻 Ortam Bilgisi
- Tarayıcı: Chrome 120
- OS: Windows 11
- Tarih: 2024-01-15
```

### Feature Request Template
```markdown
## 💡 Özellik Önerisi
Özelliğin kısa açıklaması

## 🎯 Problem/İhtiyaç
Hangi problemi çözüyor

## 💭 Önerilen Çözüm
Nasıl implement edilebilir

## 🔄 Alternatifler
Başka yaklaşımlar var mı

## 📚 Ek Bağlam
İlgili kaynaklar/örnekler
```

## 🤝 Community Guidelines

### Davranış Kuralları
- **Saygılı olun**: Farklı görüşlere saygı gösterin
- **Yapıcı olun**: Eleştirilerinizi çözüm önerisiyle destekleyin
- **Sabırlı olun**: Review süreci zaman alabilir
- **Yardımsever olun**: Yeni katkıcılara destek olun

### İletişim Kanalları
- **Issues**: Teknik konular ve bug reports
- **Discussions**: Genel tartışmalar ve sorular
- **Pull Requests**: Kod/içerik incelemesi
- **Email**: [bahattin.yunus@example.com] - Acil durumlar

### Review Süreci
1. **Otomatik kontroller**: Markdown, link kontrolü
2. **Peer review**: Community üyelerinden geri bildirim
3. **Maintainer review**: Proje yürütücüsü final onay
4. **Merge**: Ana branch'e dahil edilme

## 🏷️ Labeling System

### Priority Labels
- `priority: high` 🔴 - Acil müdahale
- `priority: medium` 🟡 - Normal öncelik  
- `priority: low` 🟢 - Düşük öncelik

### Type Labels  
- `type: bug` 🐛 - Hata raporu
- `type: feature` ✨ - Yeni özellik
- `type: docs` 📚 - Dokümantasyon
- `type: enhancement` 🚀 - İyileştirme

### Status Labels
- `status: needs-review` 👀 - İnceleme bekliyor
- `status: work-in-progress` 🚧 - Devam ediyor
- `status: ready` ✅ - Merge'e hazır

## 🎉 Teşekkür

Katkıda bulunan herkese teşekkürler! Bu proje community desteği sayesinde gelişiyor.

### Hall of Fame 🌟
<!-- Katkıda bulunanlar burada listelenecek -->
- [@bahattinyunus](https://github.com/bahattinyunus) - Proje kurucusu ve ana geliştirici

---

**Sorularınız mı var?** Issue açın veya email gönderin. Katkınız değerli! 🚀
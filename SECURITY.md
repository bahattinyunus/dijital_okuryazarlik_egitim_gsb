# Security Policy

## Güvenlik Politikası 🔒

Bu doküman, GSB Dijital Okuryazarlık Eğitimi projesinin güvenlik politikasını açıklar.

## 📋 Desteklenen Versiyonlar

Bu eğitim materyali sürekli güncellenmektedir. Güvenlik güncellemeleri için aşağıdaki versiyonlar desteklenmektedir:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < 1.0   | :x:                |

## 🚨 Güvenlik Açığı Bildirimi

Eğer bu projede bir güvenlik açığı keşfederseniz, lütfen aşağıdaki adımları izleyin:

### Hemen Bildirin

**LÜTFEN** güvenlik açıklarını public issue olarak bildirmeyin. Bunun yerine:

1. **Email ile bildirin**: [bahattin.yunus@example.com]
2. **Konu başlığı**: `[SECURITY] GSB Eğitimi - Güvenlik Açığı`
3. **24 saat içinde** yanıt alacaksınız
4. **72 saat içinde** ilk değerlendirme yapılacak

### Bildirimde Bulunması Gerekenler

```
📧 EMAIL ŞABLONU:
Konu: [SECURITY] GSB Eğitimi - Güvenlik Açığı

- Açığın detaylı açıklaması
- Etkilenen dosya/bölüm
- Potansiyel risk seviyesi
- Önerilen çözüm (varsa)
- İletişim bilgileriniz
```

### Güvenlik Açığı Kategorileri

#### 🔴 Kritik (Critical)
- Kişisel veri sızıntısı riski
- Zararlı kod injection
- System compromise potansiyeli
- **Yanıt süresi**: 24 saat

#### 🟡 Yüksek (High)  
- Hassas bilgi ifşası
- Authentication bypass
- Privilege escalation
- **Yanıt süresi**: 72 saat

#### 🟢 Orta (Medium)
- Information disclosure
- DoS vulnerabilities
- **Yanıt süresi**: 1 hafta

#### 🔵 Düşük (Low)
- Minor information leaks
- **Yanıt süresi**: 2 hafta

## 🛡️ Güvenlik Önlemleri

### Eğitim İçeriği Güvenliği

#### Kişisel Veri Koruması
- ✅ Hiçbir gerçek kişisel bilgi örnek olarak kullanılmamıştır
- ✅ Tüm örnek veriler fictitious (hayali) 
- ✅ KVKK/GDPR uyumlu content
- ✅ Çocuk güvenliği odaklı yaklaşım

#### Link ve Kaynak Güvenliği
- ✅ Tüm external linkler güvenilir kaynaklar
- ✅ Malicious content taraması yapılmış
- ✅ Phishing link kontrolü
- ✅ Safe browsing verification

#### Code ve Script Güvenliği
- ✅ Hiçbir executable code içermiyor
- ✅ Tüm kod örnekleri educational purpose
- ✅ No malicious scripts
- ✅ Safe markdown only

### Contributor Güvenliği

#### Pull Request Security
```yaml
security_checks:
  - malicious_code_scan: enabled
  - link_safety_check: enabled  
  - personal_data_detection: enabled
  - inappropriate_content_filter: enabled
```

#### Automated Security Scans
- GitHub Security Advisories
- Dependabot alerts (if applicable)
- CodeQL analysis
- Link rot detection

## 🔒 Güvenlik Best Practices

### Eğitmenler İçin

#### Classroom Security
- 🔐 **Screen sharing dikkat**: Kişisel bilgileri gizle
- 🔐 **Demo hesapları**: Gerçek hesap kullanma
- 🔐 **Student data**: Öğrenci verilerini koruma
- 🔐 **Device security**: Eğitim cihazları güvenli

#### Online Safety Education
- 🛡️ Siber güvenlik awareness
- 🛡️ Phishing education
- 🛡️ Password security
- 🛡️ Social engineering awareness

### Öğrenciler İçin

#### Digital Safety
- ⚠️ **Never share**: Gerçek kişisel bilgileri paylaşma
- ⚠️ **Demo only**: Sadece demo/test hesapları kullan
- ⚠️ **Public wifi**: Hassas işlemler yapma
- ⚠️ **Screenshot privacy**: Kişisel bilgi gösterme

## 📊 Incident Response Plan

### 1. Detection (Tespit)
- Güvenlik açığı keşfedildi
- Risk assessment yapılır
- Impact analysis

### 2. Containment (Sınırlama)  
- Immediate action
- Affected systems isolation
- Evidence preservation

### 3. Eradication (Kaldırma)
- Root cause analysis
- Vulnerability patching
- System hardening

### 4. Recovery (Kurtarma)
- Service restoration
- Monitoring enhancement
- Documentation update

### 5. Lessons Learned
- Post-incident review
- Process improvement
- Security training update

## 🔍 Security Contact

### Primary Contact
- **Name**: Bahattin Yunus Çetin
- **Email**: [bahattin.yunus@example.com]
- **Role**: Project Maintainer & Security Officer
- **Response Time**: 24 hours

### Backup Contact
- **Email**: [gsb.dijital@example.com]
- **Role**: GSB IT Security Team
- **Response Time**: 48 hours

## 🏆 Security Hall of Fame

Güvenlik açıklarını sorumlu bir şekilde bildiren kişilere teşekkürler:

<!-- Security researchers will be listed here -->
- İlk güvenlik araştırmacısı bekleniyor... 👨‍💻

## 📜 Yasal Uyarılar

### Responsible Disclosure
- Bu projede güvenlik araştırması yapabilirsiniz
- Lütfen responsible disclosure principles'ı takip edin
- Yasal sınırlar dahilinde hareket edin
- Kişisel veri gizliliğine saygı gösterin

### Legal Protection
Bu proje kapsamında güvenlik araştırması yaparken:
- ✅ Automated scanning tool'ları kullanabilirsiniz
- ✅ Static analysis yapabilirsiniz
- ❌ DoS attacks yasaktır
- ❌ Data exfiltration yasaktır
- ❌ Social engineering yasaktır

## 📚 Security Resources

### Educational Links
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Common Weakness Enumeration](https://cwe.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Turkish Cyber Security Guidelines](https://www.usom.gov.tr/)

### Tools ve Utilities
- [Security Headers](https://securityheaders.com/)
- [SSL Labs](https://www.ssllabs.com/ssltest/)
- [Have I Been Pwned](https://haveibeenpwned.com/)
- [VirusTotal](https://www.virustotal.com/)

---

**Son Güncelleme**: 19 Kasım 2024  
**Policy Version**: 1.0  
**Next Review**: 19 Mayıs 2025

> 🔒 **Güvenlik hepimizin sorumluluğudur!** Bu projeyi güvenli tutmak için işbirliği yapalım.
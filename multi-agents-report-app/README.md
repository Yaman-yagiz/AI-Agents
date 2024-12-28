# Multi-Agent LLM Sistemi Gemini API Kullanımı

## Genel Bakış

Bu proje, Gemini API kullanarak bir multi-ajandan oluşan bir sistemi uygular. Ajanlar, birbirleriyle işbirliği yaparak raporlar oluşturur. Sistem, **Customer Relation Officer** (CRO), **Author** (Report Author) ve **Editor** olmak üzere üç ajandan oluşur. Her ajan, bilgi toplama, rapor yazma, gözden geçirme ve raporu sonlandırma sürecinde farklı bir rol oynar.

## İçindekiler

- [Proje Tanımı](#proje-tanımı)
- [Ajanlar Hakkında](#ajanlar-hakkında)
- [Sistem Akışı](#sistem-akışı)
- [Gereksinimler](#gereksinimler)

---

## Proje Tanımı

Bu proje, raporların oluşturulması için işbirlikçi bir ortam yaratmayı amaçlar. **Gemini API** kullanarak, ajanlar şu sırayla görevleri yerine getirir:

1. **Customer Relation Officer (CRO)**: Kullanıcı ile etkileşime girer, rapor ihtiyaçlarını toplar ve toplanan verileri **Author**'a iletir.
2. **Author**: Alınan bilgilerle raporu taslak olarak hazırlar ve **Editor**'e gözden geçirmesi için iletir.
3. **Editor**: Raporu tamlık, doğruluk ve uygunluk açısından gözden geçirir. Gerekli görülürse **Author**'a revizyon geri bildiriminde bulunur ve rapor tamamlanana kadar bu süreci tekrarlar.

Ajanlar arasındaki iletişim, talimatların net ve düzenli bir şekilde iletilmesi sağlanır.

---

## Ajanlar Hakkında

### 1. Customer Relation Officer (CRO)
**Customer Relation Officer (CRO)**, kullanıcı ile etkileşime giren ajandır. Bu ajanın başlıca görevleri şunlardır:
- Kullanıcıdan rapor için gerekli detayları istemek.
- Eksik bilgiler olup olmadığını belirlemek ve kullanıcıdan ek bilgi talep etmek.
- Toplanan verileri, rapor yazmak için **Author**'a iletmek.

**Ana görevler:**
- Rapor konularını ve gerekli detayları toplamak.
- Gerekirse ek bilgi istemek.
- Toplanan verileri **Author**'a iletmek.

### 2. Author
**Author**, **Customer Relation Officer (CRO)**'dan gelen verileri kullanarak raporu taslak olarak yazmaya başlar. **Author**'ın başlıca görevleri şunlardır:
- **CRO**'dan gelen detaylarla raporu yazmak.
- **Editor**'den gelen geri bildirimlere göre raporu revize etmek ve rapor tatmin edici hale gelene kadar düzenlemek.

**Ana görevler:**
- İlk raporu yazmak.
- **Editor**'ün önerileri doğrultusunda raporu revize etmek.
- Hiçbir revizyon gerekmiyorsa raporu sonlandırmak.

### 3. Editor
**Editor**, **Author** tarafından yazılan raporu gözden geçiren ajandır. **Editor**'ün başlıca görevleri şunlardır:
- Raporun tamamlığını kontrol etmek ve kullanıcının beklentilerine uygun olup olmadığını değerlendirmek.
- Gerekli görüldüğünde **Author**'a revizyon talebi göndermek.

**Ana görevler:**
- Raporu gözden geçirmek.
- Gerekirse revizyon talepleri göndermek.
- Rapor tamamlandığında sonlandırmak.

---

## Sistem Akışı

1. **Customer Relation Officer** (CRO) kullanıcı ile etkileşime girer ve ihtiyaçlarını anlar.
2. **CRO**, gerekli bilgileri toplar ve **Author**'a iletir.
3. **Author**, verilen bilgilerle raporu taslak olarak yazar.
4. **Editor**, raporu gözden geçirir ve revizyon geri bildiriminde bulunur.
5. **Editor**, rapordan memnun kaldığında raporu tamamlar.

Ajanlar arasındaki etkileşim, sistemin düzenli ve net bir şekilde çalışmasını sağlar.

---

## Gereksinimler

- Python 3.8 veya daha yüksek bir sürüm
- **google-generativeai** kütüphanesi (Gemini API ile entegrasyon için)
- **python-dotenv** (çevre değişkenlerini yönetmek için)
- `requirements.txt` dosyasında listelenen diğer bağımlılıklar

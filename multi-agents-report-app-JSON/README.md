# Multi-Agent LLM Sistemi ile JSON Tabanlı Rapor Oluşturma

## Genel Bakış

Bu proje, Gemini API kullanarak JSON tabanlı iletişim protokolü üzerinden çalışan çok ajanlı bir sistem implementasyonudur. Sistem, **Customer Relation Officer** (CRO), **Author** ve **Editor** olmak üzere üç ajandan oluşur. Her ajan, belirli bir JSON yapısında veri alır ve yanıt verir.

## İçindekiler

- [Proje Tanımı](#proje-tanımı)
- [Ajanlar ve JSON Yapıları](#ajanlar-ve-json-yapıları)
- [Sistem Akışı](#sistem-akışı)
- [Gereksinimler](#gereksinimler)

## Proje Tanımı

Bu proje, raporların oluşturulması için işbirlikçi bir ortam yaratmayı amaçlar. **Gemini API** kullanarak, ajanlar şu sırayla görevleri yerine getirir:

1. **Customer Relation Officer (CRO)**: Kullanıcı ile etkileşime girer, rapor ihtiyaçlarını toplar ve toplanan verileri **Author**'a iletir.
2. **Author**: Alınan bilgilerle raporu taslak olarak hazırlar ve **Editor**'e gözden geçirmesi için iletir.
3. **Editor**: Raporu tamlık, doğruluk ve uygunluk açısından gözden geçirir. Gerekli görülürse **Author**'a revizyon geri bildiriminde bulunur ve rapor tamamlanana kadar bu süreci tekrarlar.

Ajanlar arasındaki iletişim JSON ile yapılandırılmıştır. Bu sayede, talimatların net ve düzenli bir şekilde iletilmesi sağlanır.

---

## Ajanlar ve JSON Yapıları

### 1. Customer Relation Officer (CRO)

Kullanıcı ile etkileşime girerek rapor gereksinimlerini toplar.

**JSON Çıktı Formatı:**
```json
{
    "action": "continue | done",
    "message": "Kullanıcıya sorulacak soru veya mesaj",
    "summary": {
        "topic": "rapor konusu",
        "purpose": "raporun amacı",
        "target_audience": "hedef kitle",
        "key_points": ["nokta1", "nokta2"],
        "special_requirements": ["gereksinim1", "gereksinim2"],
        "tone": "formal/informal/technical",
        "length_requirement": "beklenen uzunluk"
    }
}
```

### 2. Author

CRO'dan gelen gereksinimlere göre raporu oluşturur.

**JSON Çıktı Formatı:**
```json
{
    "action": "done",
    "report": {
        "content": "markdown formatında rapor içeriği",
        "sections": ["bölüm1", "bölüm2"],
        "word_count": "kelime sayısı",
        "metadata": {
            "tone": "kullanılan ton",
            "target_audience": "hedef kitle",
            "key_points_covered": ["kapsanan nokta1", "kapsanan nokta2"]
        }
    }
}
```

### 3. Editor

Raporu gözden geçirir ve gerekli geribildirimleri sağlar.

**JSON Çıktı Formatı:**
```json
{
    "action": "revise | done",
    "feedback": {
        "general_comments": "genel değerlendirme",
        "specific_issues": ["sorun1", "sorun2"],
        "improvement_suggestions": ["öneri1", "öneri2"],
        "strengths": ["güçlü yön1", "güçlü yön2"],
        "alignment_score": "1-10 arası puan",
        "quality_score": "1-10 arası puan"
    }
}
```

## Sistem Akışı

1. **Başlangıç Aşaması**
   - CRO kullanıcı ile etkileşime girer
   - Kullanıcının dilini algılar ve o dilde iletişim kurar
   - Rapor gereksinimlerini JSON formatında toplar

2. **Rapor Yazım Aşaması**
   - Author, CRO'dan gelen JSON verileri işler
   - Markdown formatında rapor oluşturur
   - JSON yapısında metadata ile birlikte raporu iletir

3. **Değerlendirme Aşaması**
   - Editor raporu inceler
   - JSON formatında detaylı geri bildirim sağlar
   - Revizyon gerekiyorsa `"action": "revise"` ile belirtir

4. **Revizyon Döngüsü**
   - Author, Editor'ün JSON geri bildirimlerine göre raporu günceller
   - Bu döngü maksimum 5 kez tekrarlanabilir
   - Editor onay verene kadar devam eder

5. **Sonlandırma**
   - Onaylanan rapor Markdown ve Word formatlarında kaydedilir
   - Kullanıcıya final rapor teslim edilir

## Gereksinimler

### Teknik Gereksinimler
- Python 3.8+
- google-generativeai
- python-dotenv
- markdown2
- python-docx

## Önemli Notlar

- **Rapor Gereksinimleri**
  - Minimum 3000, maksimum 5000 kelime
  - Markdown formatında yazılır
  - Word belgesine otomatik dönüştürülür

- **Sistem Özellikleri**
  - Çok dilli destek
  - JSON tabanlı iletişim
  - Maksimum 5 revizyon hakkı
  - Otomatik format dönüşümü

- **Hata Yönetimi**
  - JSON parse hataları ele alınır
  - API bağlantı hataları yönetilir
  - Kullanıcı kesintileri (KeyboardInterrupt) yakalanır

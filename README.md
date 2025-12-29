# 🌬️ Rüzgar Türbini Güç Üretim Tahmin Sistemi (Wind Turbine Power Prediction)

Bu proje, rüzgar türbinlerine ait **SCADA (Supervisory Control and Data Acquisition)** verilerini kullanarak, türbinin anlık güç üretimini makine öğrenmesi algoritmalarıyla yüksek doğrulukla tahmin etmeyi amaçlar. Geliştirilen en başarılı model, **Streamlit** tabanlı interaktif bir web arayüzüne entegre edilmiştir.

## 🎯 Projenin Amacı
Rüzgar enerjisinin değişken ve stokastik yapısını analiz ederek, enerji üretim planlamasına yardımcı olacak güvenilir bir tahmin mekanizması oluşturmaktır. Proje kapsamında ham veri temizlenmiş, **Linear Regression**, **XGBoost** ve **LightGBM** modelleri kıyaslanmış ve **%96.80** başarı oranına ulaşılmıştır.

## 📊 Veri Seti ve Ön İşleme
Kullanılan veri seti 50.530 satır SCADA verisinden oluşmaktadır.
* **Öznitelikler:** Tarih/Saat, Rüzgar Hızı (m/s), Rüzgar Yönü (°), Teorik Güç Eğrisi (KWh) ve Aktif Güç (kW).
* **Veri Temizliği:** Rüzgar hızının yüksek olduğu (>3 m/s) ancak üretimin olmadığı (<= 20 kW) anomali durumları (arıza/bakım) tespit edilerek veri setinden çıkarılmıştır.
* **Feature Engineering:** Zaman damgası; Ay, Gün ve Saat olarak ayrıştırılarak modelin mevsimsel döngüleri öğrenmesi sağlanmıştır.

## 🧠 Kullanılan Modeller ve Sonuçlar 
Projede üç farklı model eğitilmiş ve performansları karşılaştırılmıştır. **LightGBM**, hem hız hem de doğruluk açısından en iyi performansı gösteren model olarak seçilmiştir.

| Model | R² Skoru | MAE (Ortalama Hata) | RMSE (Karesel Hata) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Regression** | 0.9634 | 129.52 kW | 250.22 kW | Baseline |
| **XGBoost** | 0.9661 | 97.70 kW | 241.04 kW | İyi Performans |
| **LightGBM** | **0.9680** | **97.39 kW** | **234.21 kW** | 🏆 **Seçilen Model** |

## 💻 Teknoloji Yığını (Tech Stack)
* **Dil:** Python 3.13
* **Veri Analizi:** Pandas, NumPy
* **Görselleştirme:** Matplotlib, Seaborn
* **Makine Öğrenmesi:** Scikit-learn, XGBoost, LightGBM
* **Arayüz (GUI):** Streamlit
* **Model Kayıt:** Joblib

## 🚀 Kurulum ve Kullanım

1.  Repoyu klonlayın:
2.  Gerekli kütüphaneleri yükleyin:
3.  Gerekli dosya yollarını kendi yolunuza göre ayarlayın
4.  Uygulamayı çalıştırın:
    ```bash
    streamlit run [app.py dosyasının yolu]
    ```

## 👥 Takım Üyeleri
* **Kaan Pulat** - Veri Analizi, Modelleme, Arayüz,  Dokümantasyon ve Kontrol
* **Eren Akca** - Veri Temizleme, Modelleme, Arayüz, Dokümantasyon ve Kontrol

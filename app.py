import streamlit as st
import joblib
import numpy as np
from datetime import datetime

# --- SAYFA YAPISI ---
st.set_page_config(
    page_title="Rüzgar Enerjisi Tahmin",
    page_icon="🌬️",
    layout="wide"
)

# --- ÖZEL CSS ---
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .result-box {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .result-value {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    .info-card {
        background: #f8f9fa;
        padding: 1rem;
        border-left: 4px solid #667eea;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
st.markdown("""
    <div class="main-header">
        <h1>🌬️ Rüzgar Enerjisi Güç Tahmin Sistemi</h1>
        <p>Yapay Zeka Destekli Enerji Üretim Tahmini</p>
    </div>
""", unsafe_allow_html=True)

# --- MODEL YÜKLEME ---
@st.cache_resource
def load_model():
    return joblib.load('D:\Dersler\Veri_Bilimi\Projev4\Model_Sonuclar\lightgbm_model_wdate.joblib')

model = load_model()

# --- ANA BÖLÜM ---
main_col1, main_col2 = st.columns([2, 1])

with main_col1:
    st.markdown("### 📅 Tarih ve Zaman Seçimi")
    
    date_time_col1, date_time_col2 = st.columns(2)
    with date_time_col1:
        selected_date = st.date_input(
            "Tahmin Tarihi", 
            value=datetime.now().date(), 
            key="date_picker",
            help="Tahmin yapmak istediğiniz tarihi seçin"
        )
    with date_time_col2:
        selected_time = st.time_input(
            "Tahmin Saati", 
            value=datetime.now().time(), 
            key="time_picker",
            help="Tahmin yapmak istediğiniz saati seçin"
        )
    
    st.markdown("---")
    st.markdown("### 🌪️ Meteorolojik Parametreler")
    
    param_col1, param_col2, param_col3 = st.columns(3)
    
    with param_col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        wind_speed = st.number_input(
            "Rüzgar Hızı", 
            min_value=0.0, 
            value=5.0, 
            key="ws",
            help="Rüzgar hızını m/s cinsinden girin"
        )
        st.markdown("**m/s**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with param_col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        theoretical_curve = st.number_input(
            "Teorik Güç Eğrisi", 
            min_value=0.0, 
            value=400.0, 
            key="tc",
            help="Teorik güç eğrisi değerini KWh cinsinden girin"
        )
        st.markdown("**KWh**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with param_col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        wind_direction = st.number_input(
            "Rüzgar Yönü", 
            min_value=0.0, 
            max_value=360.0, 
            value=250.0, 
            key="wd",
            help="Rüzgar yönünü derece cinsinden girin (0-360)"
        )
        st.markdown("**°**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    predict_button = st.button("⚡ TAHMİN ET", use_container_width=True)
    
    if predict_button:
        with st.spinner("Model hesaplama yapıyor..."):
            h = selected_time.hour
            m = selected_date.month
            d = selected_date.weekday()
            
            input_features = np.array([[wind_speed, theoretical_curve, wind_direction, h, m, d]])
            prediction = model.predict(input_features)[0]
            prediction = max(0, prediction)
            
            st.markdown(f"""
                <div class="result-box">
                    <h2>Tahmin Sonucu</h2>
                    <div class="result-value">{prediction:.2f} kW</div>
                    <p style="color: white; margin-top: 1rem;">Beklenen Güç Üretimi</p>
                </div>
            """, unsafe_allow_html=True)

with main_col2:
    st.markdown("### 🔍 Anlık Bilgiler")
    
    # Tarih Bilgisi
    st.info(f"""
**📅 Tarih Bilgisi**

**Tarih:** {selected_date.strftime('%d.%m.%Y')}  
**Ay:** {selected_date.month}  
**Gün:** {['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar'][selected_date.weekday()]}
    """)
    
    # Zaman Bilgisi
    st.info(f"""
**🕐 Zaman Bilgisi**

**Saat:** {selected_time.strftime('%H:%M')}  
**Saat Dilimi:** {selected_time.hour}:00
    """)
    
    # Model Bilgisi
    st.info("""
**ℹ️ Model Bilgisi**

**Model:** LightGBM v2  
**Feature Sayısı:** 6  
**Accuracy:** Yüksek
    """)
    
    # İpuçları
    st.info("""
**💡 İpuçları**

• Gerçekçi değerler girin  
• Rüzgar yönü 0-360° arası  
• Farklı senaryolar deneyin
    """)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🌱 Temiz Enerji için Yapay Zeka | Geliştirici: Veri Bilimi Projesi</p>
    </div>
""", unsafe_allow_html=True)
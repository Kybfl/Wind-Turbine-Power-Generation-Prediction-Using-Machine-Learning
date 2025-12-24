import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# --- AYARLAR ---
clean_dataset = pd.read_csv('Dataset_Clean.csv')  # Temizlenmiş veri dosyasının yolu

# 1. VERİYİ HAZIRLAMA 
# Normalizasyon yok.
X = clean_dataset.drop(['LV ActivePower (kW)', 'Date/Time'], axis=1)
y = clean_dataset['LV ActivePower (kW)']

# 2. TRAIN - TEST AYRIMI
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. XGBOOST MODELİNİ KURMA
# n_estimators=1000: 1000 tane düzeltici ağaç kur.
# learning_rate=0.05: Her ağacın katkısını %5 ile sınırla (daha güvenli öğrenme).
print("XGBoost eğitimi başlıyor...")
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', 
                             n_estimators=1000, 
                             learning_rate=0.05, 
                             n_jobs=-1, # Tüm işlemci çekirdeklerini kullan
                             random_state=42)

xgb_model.fit(X_train, y_train)

# 4. TAHMİN VE METRİKLER
y_pred_xgb = xgb_model.predict(X_test)

r2 = r2_score(y_test, y_pred_xgb)
mae = mean_absolute_error(y_test, y_pred_xgb)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_xgb))

print(f"\n--- XGBoost Sonuçları ---")
print(f"R² Skoru: {r2:.4f}")
print(f"MAE: {mae:.2f} kW")
print(f"RMSE: {rmse:.2f} kW")

# 5. MODELİ KAYDETME
joblib.dump(xgb_model,'xgboost_model.joblib')

import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# --- AYARLAR ---
clean_dataset = pd.read_csv('Dataset_Clean.csv')  # Temizlenmiş veri dosyasının yolu


# 1. VERİYİ HAZIRLAMA
X = clean_dataset.drop(['LV ActivePower (kW)', 'Date/Time'], axis=1)
y = clean_dataset['LV ActivePower (kW)']

# 2. TRAIN - TEST AYRIMI
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. LIGHTGBM MODELİNİ KURMA
print("LightGBM eğitimi başlıyor...")
lgb_model = lgb.LGBMRegressor(n_estimators=1000, 
                              learning_rate=0.05, 
                              n_jobs=-1, 
                              random_state=42)

lgb_model.fit(X_train, y_train)

# 4. TAHMİN VE METRİKLER
y_pred_lgb = lgb_model.predict(X_test)

r2 = r2_score(y_test, y_pred_lgb)
mae = mean_absolute_error(y_test, y_pred_lgb)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_lgb))

print(f"\n--- LightGBM Sonuçları ---")
print(f"R² Skoru: {r2:.4f}")
print(f"MAE: {mae:.2f} kW")
print(f"RMSE: {rmse:.2f} kW")

# 5. KAYDETME
joblib.dump(lgb_model,'lightgbm_model.joblib')

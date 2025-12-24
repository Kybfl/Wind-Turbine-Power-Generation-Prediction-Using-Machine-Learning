import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # Normalizasyon için
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib # Modeli kaydetmek için

# 1. VERİYİ HAZIRLAMA
clean_data = pd.read_csv('Dataset_Clean.csv')  # Temizlenmiş veri dosyasını yükle

# df temizlenmiş veri seti
X = clean_data.drop(['LV ActivePower (kW)', 'Date/Time'], axis=1) # Hedef ve tarih dışındakiler
y = clean_data['LV ActivePower (kW)'] # Tahmin etmek istediğimiz değer


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression için StandardScaler Ortalama=0, Std. Sapma=1 
scaler = StandardScaler()

# Scaler'ı sadece X_train üzerinde eğitiyoruz.
# Sonra bu öğrendiği kuralı hem X_train'e hem X_test'e uyguluyoruz.
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

y_pred_lr = lr_model.predict(X_test_scaled)

r2 = r2_score(y_test, y_pred_lr)
mae = mean_absolute_error(y_test, y_pred_lr)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))

print(f"--- Linear Regression Sonuçları ---")
print(f"R² Skoru (Başarı Oranı): {r2:.4f}")
print(f"MAE (Ortalama Mutlak Hata): {mae:.2f} kW")
print(f"RMSE (Kök Ortalama Kare Hata): {rmse:.2f} kW")

# 7. MODELİ VE SCALER'I KAYDETME 
# Sadece modeli değil, scaler'ı da kaydetmeliyiz. Çünkü yeni veri gelince de scale etmemiz gerekecek.
joblib.dump(lr_model, 'linear_regression_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
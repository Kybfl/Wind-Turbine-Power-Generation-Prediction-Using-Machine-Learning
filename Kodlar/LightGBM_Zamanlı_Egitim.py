import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Veriyi yükle
df = pd.read_csv('Dataset_With_Time.csv')

# 1. ÖZELLİK SEÇİMİ (Zaman özellikleri dahil)
features = ['Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)', 'Wind Direction (°)', 'hour', 'month', 'day_of_week']
X = df[features]
y = df['LV ActivePower (kW)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. HİPERPARAMETRE OPTİMİZASYONU (Yönerge gereği zorunlu)
print("Optimizasyon başlatılıyor...")
param_grid = {
    'n_estimators': [500, 1000],
    'learning_rate': [0.05, 0.1],
    'num_leaves': [31, 50]
}

lgb_model = lgb.LGBMRegressor(random_state=42)
grid_search = GridSearchCV(estimator=lgb_model, param_grid=param_grid, cv=3, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)

# 3. EN İYİ MODEL VE SONUÇLAR
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print(f"\nEn İyi Parametreler: {grid_search.best_params_}")
print(f"R² Skoru: {r2_score(y_test, y_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} kW")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} kW")

# 4. KAYDETME
joblib.dump(best_model, 'lightgbm_model_wdate.joblib')
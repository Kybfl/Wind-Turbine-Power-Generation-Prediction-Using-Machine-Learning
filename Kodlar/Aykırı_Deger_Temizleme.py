import pandas as pd
import numpy as np

dataset = pd.read_csv('Dataset.csv')

# Aykırı değer temizleme öncesi satır sayısı
initial_shape = dataset.shape[0]

# 1. Anomali Koşulunu Sağlayan Satırları Bulma
anomaly_condition = (dataset['Wind Speed (m/s)'] > 3) & (dataset['LV ActivePower (kW)'] <= 20)
anomalies = dataset[anomaly_condition]

# print(f"Başlangıç Satır Sayısı: {initial_shape}")
# print(f"Tespit Edilen Anomali Sayısı: {len(anomalies)}")

# print("\nTespit Edilen Anomali Satırlarından İlk 5 Örnek:")
# print(anomalies.head())


# Tilda (~) operatörü ile koşulu sağlamayanları (yani anomalileri) hariç tutarız.
dataset_clean = dataset[~anomaly_condition]
dataset_clean.to_csv('Dataset_Clean.csv', index=False)
# Temizleme sonrası satır sayısını ve düşen satır sayısını kontrol et
removed_rows = initial_shape - dataset_clean.shape[0]

print(f"Başlangıç Satır Sayısı: {initial_shape}")
print(f"Temizleme Sonrası Satır Sayısı: {dataset_clean.shape[0]}")
print(f"Kaldırılan Anomali Satır Sayısı: {removed_rows}")







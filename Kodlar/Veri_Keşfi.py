import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('Dataset.csv')
numeric_df = dataset.select_dtypes(include=['int64', 'float64']) # Sadece sayısal sütunları seç

print("\nVeri Setinin Sütun İsimleri:")
print(dataset.columns.tolist())

print("\nVeri Setinin Boyutu (Satır, Sütun):")
print(dataset.shape)

print("Veri Setinin İlk 5 Satırı:")
print(dataset.head())

print("\nVeri Setinin Temel İstatistikleri:")
print(dataset.describe())

print("\nVeri Setindeki Eksik Değerler:")
print(dataset.isnull().sum())

print("\nVeri Setindeki Veri Tipleri:")
print(dataset.dtypes)

print("\nVeri Setindeki Benzersiz Değer Sayısı:")
print(dataset.nunique())

print("Çift Değerli Satır Sayısı:")
print(f"{dataset.duplicated().sum()} adet çift değerli satır bulundu.")

corr = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.scatterplot(x='Wind Speed (m/s)', y='LV ActivePower (kW)', data=dataset, alpha=0.5, color='dodgerblue')
plt.title('Rüzgar Hızı ve Gerçek Güç Üretimi Dağılımı', fontsize=14)
plt.xlabel('Rüzgar Hızı (m/s)', fontsize=12)
plt.ylabel('Aktif Güç (kW)', fontsize=12)
plt.show()
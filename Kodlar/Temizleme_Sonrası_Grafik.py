import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

Dataset_Clean = pd.read_csv('Dataset_Clean.csv')
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.scatterplot(x='Wind Speed (m/s)', y='LV ActivePower (kW)', data=Dataset_Clean, alpha=0.5, color='blueviolet')
plt.title('Temizleme Sonrası Rüzgar Hızı ve Gerçek Güç Üretimi Dağılımı', fontsize=14)
plt.xlabel('Rüzgar Hızı (m/s)', fontsize=12)
plt.ylabel('Aktif Güç (kW)', fontsize=12)
plt.show()
import pandas as pd

# Veriyi yükle
df = pd.read_csv('Dataset_Clean.csv')

# Tarih sütununu datetime formatına çevir
df['Date/Time'] = pd.to_datetime(df['Date/Time'], dayfirst=True)

# Zaman özelliklerini çıkar
df['hour'] = df['Date/Time'].dt.hour
df['month'] = df['Date/Time'].dt.month
df['day_of_week'] = df['Date/Time'].dt.dayofweek

# Yeni dosyayı kaydet
df.to_csv('Dataset_With_Time.csv', index=False)
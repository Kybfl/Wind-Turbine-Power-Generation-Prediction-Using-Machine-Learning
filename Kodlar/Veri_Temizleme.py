import pandas as pd

dataset = pd.read_csv('Dataset.csv')
numeric_df = dataset.select_dtypes(include=['int64', 'float64']) # Sadece sayısal sütunları seç

print("Eksik Veri Durumu:")
print(dataset.isnull().sum())



import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

customer_df = pd.read_csv('customer_details.csv')
basket_df = pd.read_csv('basket_details.csv')

cinsiyet_ortalama = customer_df["sex"].value_counts(normalize=True) * 100
print(cinsiyet_ortalama)
#.mul(100).plot.pie(autopct = '%.1f%%') 

plt.figure(figsize = (4,4))
cinsiyet_ortalama.plot(kind = 'bar', color = ['red', 'blue'], edgecolor = 'black')
plt.xlabel('cinsiyet')
plt.ylabel('Oran')
plt.xticks(rotation = 0)
plt.grid(axis='y', alpha=0.1)
plt.show()

yas_ortalama = customer_df['customer_age'].mean().astype(int)
print("Ortalama Yaş:", yas_ortalama)

basket_df['yil'] =pd.to_datetime(basket_df['basket_date']).dt.year
basket_df['ay'] =pd.to_datetime(basket_df['basket_date']).dt.month
basket_df['gün'] =pd.to_datetime(basket_df['basket_date']).dt.day

aylik_siparis = basket_df.groupby('ay')['product_id'].count().plot.pie(autopct = '%.1f%%')
print(aylik_siparis)

günlük_siparis = basket_df.groupby('gün')['product_id'].count().idxmax()
print("En cok siparis verilen gun:",günlük_siparis)

toplam_satis = basket_df.groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(5).plot.pie(autopct = '%.1f%%')
print("En cok satilan 5 urun:\n",toplam_satis)

top_müsteri = basket_df['customer_id'].value_counts().head(5)
print("En cok alisveris yapan 5 musteri:\n",top_müsteri)

satis = basket_df.groupby('basket_date')['basket_count'].sum().sort_values(ascending=False).head(5).plot.pie(autopct = '%.1f%%')
print("En yuksek satis yapilan 5 tarih:\n",satis)

#Yaş gruplarına göre satış analizi
customer_df['customer_age'] = pd.to_numeric(customer_df['customer_age'], errors='coerce')
customer_df['customer_age'].fillna(customer_df['customer_age'].median(), inplace=True)

bins = [0, 18, 30, 45, 60, 3000]
labels = ['0-18', '19-30', '31-45', '46-60', '60+']
customer_df['yas_grubu'] = pd.cut(customer_df['customer_age'], bins=bins, labels=labels)

merged = basket_df.merge(customer_df, on='customer_id')
yas_satis = merged.groupby('yas_grubu')['basket_count'].sum()

yas_satis.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Yaş Gruplarına Göre Satış Sayısı')
plt.xlabel('Yaş Grubu')
plt.ylabel('Toplam Satış')
plt.show()

#Cinsiyete göre en popüler ürünler
populer_urunler = merged.groupby(['sex', 'product_id'])['basket_count'].sum().reset_index()
populer_urunler = populer_urunler.sort_values(['sex','basket_count'], ascending=[True,False]).groupby('sex').head(10)
print(populer_urunler)

zaman_trendi = basket_df.groupby('basket_date')['basket_count'].sum()
zaman_trendi.plot(figsize=(8,4))
plt.title('Zamana Göre Satış Eğilimi')
plt.xlabel('Tarih')
plt.ylabel('Satış Sayısı')
plt.grid(True, alpha=0.3)
plt.show()

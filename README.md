# Proje 1 — E‑Ticaret Satış Veri Analizi

## Özet

Bu projenin amacı bir e‑ticaret sitesine ait satış verilerini analiz ederek satış performansını, popüler ürünleri ve yaş/cinsiyet bazlı dağılımları ortaya koymaktır.

---

## İçerik ve Dosya Yapısı

* `proje_1.py ve proje_2.ipynb` — Analiz kodları 
* `customer_details.csv` — Müşteri bilgileri 
* `basket_details.csv` — Sepet / işlem kayıtları 
* `README.md` — Projeyi, kullanım talimatlarını ve analiz adımlarını açıklar.
* `requirements.txt` — Gereksinimler 

[Kullanılan veri setini buradan bulabilirsiniz.](https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset/data)

> Not: proje_1.py dosyasını okuması daha rahat olması için ekledim. proje_1.ipynb dosyası daha detaylı sonuçlar içeriyor.

---

## Veri Kümeleri

**Customer Details (`customer_details.csv`)**

* `customer_id` : Müşteri ID
* `sex` : Cinsiyet
* `customer_age` : Müşteri yaşı
* `tenure` : Müşteri platformunda geçen süre (ay)

**Basket Details (`basket_details.csv`)**

* `customer_id` : Müşteri ID 
* `product_id` : Ürün ID
* `basket_date` : İşlem tarihi
* `basket_count` : Aynı günde tekrar eden aynı işlemlerin sayısı

---

## Kurulum & Gereksinimler

Aşağıdaki paketler kullanıldı:
* Python 3.11.0
* pandas
* numpy
* matplotlib

Kurulum için aşağıdaki kodları terminalde çalıştırın:
* Öncelikle projeyi cihazınıza klonlayın:
```bash
git clone https://github.com/MKalbisen/Proje_1
```
* Gereklilikleri yükleyin:
```bash
pip install -r .\requirements.txt
```

---

## Nasıl Çalıştırılır

1. `customer_details.csv` ve `basket_details.csv` dosyalarını proje klasörüne koyun.
2. `proje_1.ipynb` dosyasındaki hücreleri sırayla çalıştırın:

---

## Yapılan Analizler 

Aşağıdaki analizler proje kodunda yer alır;

1. **Cinsiyet dağılımı**

   * `sex.value_counts(normalize=True)` ile cinsiyet oranları. Grafikte bar plot ile gösterildi.
2. **Ortalama yaş**

   * `customer_age.mean()` hesaplandı.
3. **Aylık / Günlük sipariş dağılımı**

   * `groupby('ay')['product_id'].count()` ve `groupby('gün')['product_id'].count()` ile en yoğun gün/ay belirlendi.
4. **En çok satılan ürünler**

   * `groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(5)`
5. **En çok alışveriş yapan müşteriler**

   * `customer_id` bazlı `value_counts()` ile üst 5 müşteri.
6. **Yaş grubuna göre toplam satış**

   * `merged.groupby('yas_grubu')['basket_count'].sum()` → hangi yaş grubunun daha fazla satın aldığı.
7. **Cinsiyete göre en popüler ürünler**

   * `merged.groupby(['sex','product_id'])['basket_count'].sum()` → cinsiyete göre top N ürün.
8. **Zaman serisi: satış trendi**

   * `groupby('basket_date')['basket_count'].sum()` → zamanla satış eğilimi grafiği.


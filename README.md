# Döviz Dönüştürücü (Currency Converter)

Bu Python uygulaması, kullanıcıdan aldığı iki para birimi ve miktara göre güncel döviz kurları üzerinden dönüşüm yapar. Döviz kurları **[ExchangeRate-API](https://www.exchangerate-api.com/)** üzerinden alınmaktadır.

## 🚀 Özellikler

- Kullanıcıdan dönüştürmek istediği para birimlerini ve miktarı alır
- API üzerinden en güncel döviz kurlarını çeker
- Sonucu kullanıcıya gösterir
- Hatalı girişlerde kullanıcıyı uyarır

## 🧾 Desteklenen Para Birimleri

Bazı Para Birimleri: CHF, CNY, EUR, GBP, JPY, RUB, TRY, USD...

> Tüm desteklenen para birimleri, ExchangeRate-API tarafından sağlanmaktadır.

## 🛡️ API Anahtarı

Kodda örnek bir API anahtarı (`4d74e361a2c50968c1e34daa`) kullanılmıştır. Daha güvenli ve uzun vadeli kullanım için kendi anahtarınızı [ExchangeRate-API](https://www.exchangerate-api.com/) üzerinden ücretsiz bir şekilde alabilirsiniz. Aldığınız API anahtarını main.py içerisindeki aşağıda belirtilen satırı bulup API-ANAHTARINIZ yazan kısma aldığınız API anahtarını yazın.

```python
api = f"https://v6.exchangerate-api.com/v6/API-ANAHTARINIZ/latest/{fromCurrency}"
```
> Ücretsiz API ile ayda 1500 sorgu yapma sınırınız bulunmaktadır.

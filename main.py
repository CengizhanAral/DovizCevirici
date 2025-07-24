import requests

print("Desteklenen para birimleri:")
print("AUD, CAD, CHF, CNY, DKK, EUR, GBP, HKD, ILS, INR, JPY, MXN, NZD, RUB, SEK, SKD, TRY, USD...")
x = True

# 3 haneli dönüştürülecek para biriminin kısaltması
fromCurrency = input("Çevirmek istediğiniz para biriminin kısaltması: ")
# 3 haneli dönüştürülmüş para birimi kısaltması
toCurrency = input("Hangi para birimi olarak istediğinizin kısaltması: ")

while x:
    # Dönüştürülecek miktar (sayı olarak)
    money = input(f"Kaç {fromCurrency} birimindeki paranın {toCurrency} karşılığını öğrenmek istiyorsunuz? ")
    try:
        money = float(money)
        x = False
    except ValueError:
        print("Lütfen para miktarını doğru biçimde giriniz.")

api = f"https://v6.exchangerate-api.com/v6/4d74e361a2c50968c1e34daa/latest/{fromCurrency}"
getapi = requests.get(api)
if getapi.status_code == 200:
    data = getapi.json()

    currencyList = data.get("conversion_rates", {})

    for currency, rate in currencyList.items():
        if toCurrency == currency:
            currencyCalculate = money * float(rate)
            print(f"{money} {fromCurrency} = {currencyCalculate} {currency}")
else:
    print("Hata oluştu! Hata kodu:", getapi.status_code)
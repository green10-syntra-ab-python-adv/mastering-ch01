# korting.py
# voorbeeld van continue

from datetime import date, timedelta

vandaag = date.today()
morgen = vandaag + timedelta(days=1)  

producten = [
    {'code': '1', 'vervaldag': vandaag, 'prijs': 100.0},
    {'code': '2', 'vervaldag': morgen, 'prijs': 50},
    {'code': '3', 'vervaldag': vandaag, 'prijs': 20},
]
for product in producten:
    if product['vervaldag'] != vandaag:
        continue              # in dit geval mag je de loop hernemen
    product['prijs'] *= 0.8   # anders is er 20% korting
    print(
        'Prijs voor product met code', product['code'],
        'is nu', product['prijs'])                      

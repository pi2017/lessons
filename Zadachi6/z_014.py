# Программа конвертер валют (евро, доллар, гривна, рубль) перевод из любой валюты в любую.
from decimal import *

exchange_courses = {'UAH': Decimal(26.0), 'USD': Decimal(1.0), 'EUR': Decimal(0.8), 'RUB': Decimal(60.0)}
source_currency = input('Введите валюту ')
destination_currency = input('В какую валюту обменять? ')
amount = Decimal(input('Введите сумму обмена '))

amount_in_dollars = amount / exchange_courses[source_currency]
amount_in_currency = amount_in_dollars * exchange_courses[destination_currency]
print(amount, source_currency)
print(round(amount_in_currency, 2))

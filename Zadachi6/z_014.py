# Программа конвертер валют (евро, доллар, гривна, рубль) перевод из любой валюты в любую.
from typing import Dict

spisok_valuta = {'UAH': 1, 'USD': 1, 'EURO': 1, 'RUBL': 1}
koef_obmena = {'UAH': 1, 'USD': 26, 'EURO': 30, 'RUBL': 2.5}
name_valuta = input('Введите валюту ')
number_valuta = int(input('Введите сумму обмена '))
to_valuta = input('В какую валюту обменять? ')

result_valuta = number_valuta / koef_obmena.get(to_valuta)

print('-' * 23)
print(number_valuta, name_valuta, ' = ', result_valuta, to_valuta)
print('-' * 23)

#
#
# Обмен валют с обработчиком ошибок

from decimal import *

exchange_courses = {'UAH': Decimal(26.0), 'USD': Decimal(1.0), 'EUR': Decimal(0.8), 'RUB': Decimal(60.0)}


def currency_exchange():
    source_currency = input('Введите валюту ')
    destination_currency = input('В какую валюту обменять? ')
    amount = Decimal(input('Введите сумму обмена '))

    try:
        amount_in_dollars = amount / exchange_courses[source_currency]
        amount_in_currency = amount_in_dollars * exchange_courses[destination_currency]
    except KeyError:
        print('*' * 20)
        print('Not a true currency ')
        print('*' * 20)

    return amount_in_currency


print(round(currency_exchange(), 2))

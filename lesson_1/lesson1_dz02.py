# Zadacha 02

import datetime

now = datetime.datetime.now()

b_year = int(input('Введите год рождения : '))

print("Текущий год : %d" % now.year)
print('Год рождения :', b_year)
print('Ваш возраст :', now.year - b_year)

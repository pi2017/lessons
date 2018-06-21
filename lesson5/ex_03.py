#
# Списки - изменяемые последовательности любого типа данных
# Кортеж - не изменяемый список, ограниченный список
from typing import Tuple

my_list = []
my_list_0 = [1, 4, 5, 32, 88]

for i in range(10):
    my_list.append(None)

print(my_list)

my_list.insert(0, 'ausweis')

print(my_list)

my_tuple_1 = (1, 2, 'ausweis')
print(my_tuple_1)

a, b, c = 13, 13, 13
print((a, b, c))



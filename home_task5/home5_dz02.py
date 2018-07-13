# Задача 2
# Написать функцию, которая выводит двухмерный список в виде таблицы
# >>print_list([[222, 113], [456, 500]])
'''
—————
| 222 | 113 |
—————
| 456 | 500 |
—————
'''

import random


def print_list(size, min_value, max_value):
    array = [[[] for j in range(size)] for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            array[i][j] = random.randint(min_value, max_value)

    return array


result = print_list(size=2, min_value=100, max_value=999)

print('-' * 14)
print('|', result[0], '|')
print('|', result[1], '|')
print('-' * 14)

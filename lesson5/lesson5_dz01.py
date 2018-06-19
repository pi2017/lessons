# Задача 1
# Написать функцию, которая генерирует список списков (двухмерный массив) размерности NxN
# заполненный случайными числами от 100 (A) до 999 (B)

import random


def generate_list_of_lists(size, min_value, max_value):
    array = [[[] for j in range(size)] for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            array[i][j] = random.randint(min_value, max_value)

    return array


result = generate_list_of_lists(size=100, min_value=100, max_value=999)
print(result)
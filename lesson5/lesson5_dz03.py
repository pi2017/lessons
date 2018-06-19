# Задача 3
# Сгенерировать список размером 10х10 с помощью функции задания 1
# - Заменить по главной диагонали все числа на 0
# - Заменить все четные числа на 1, не четные на 0
# - Вывести строку таблицы с максимальной суммой элементов
# - Повернуть таблицу на 90 градусов, по часовой, против часовой

import random


def generate_list_of_lists(size, min_value, max_value):
    array = [[[] for j in range(size)] for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            array[i][j] = random.randint(min_value, max_value)

    return array


result = generate_list_of_lists(size=10, min_value=100, max_value=999)
print(result[0])
print(result[2])
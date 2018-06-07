# Решение домашней задачи 5
# Написать функцию, которая выводит на экран n первых четных чисел.

def is_even(lower, upper):
    for i in range(lower, upper + 1):

        if (i % 2) == 0:
            print(i)


lower = int(input('low = '))
upper = int(input('upper = '))

is_even(lower, upper)

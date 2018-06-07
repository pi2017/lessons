# Решение домашней задачи 4
# Вывести на экран 10 первых простых чисел используя функцию задания 3
# Вывести на экран, из диапазона, простые числа используя функцию задания 3


def is_prime(lower, upper):
    for i in range(lower, upper + 1):
        if i > 1:
            for j in range(2, int(i / 2)):
                if (i % j) == 0:
                    break
            else:
                print(i)

lower = int(input('low = '))
upper = int(input('upper = '))

is_prime(lower, upper)

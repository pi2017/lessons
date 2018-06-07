# Решение домашней задачи
# Написать функцию, которая определяет количество разрядов введенного целого числа.

def len_digits(x):
    x = abs(x)

    if x < 10:
        return 1

    return 1 + len_digits(x / 10)


x = int(input('x = ', ))
print ('Количество разрядов ', len_digits(x))

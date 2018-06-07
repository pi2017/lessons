# Решение домашней задачи 3
# Написать функцию is_prime(a), Которая принимает число и возвращает True или False в зависимости от того,
# простое это число или нет

def is_prime():
    n = int(input('n = '))

    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False

    return True


if is_prime():
    print("True")
else:
    print('False')

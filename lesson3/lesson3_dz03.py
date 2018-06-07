
# Решение домашних задачи 3

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

# Если два числа равны то умножаем все три на 5

a = int(input("введите первое число a :"))
b = int(input("введите второе число b :"))
c = int(input("введите третье число c :"))

if a == b or a == c:
    print('{}x{}={}\t'.format(a, 5, a * 5), end='')
    print('{}x{}={}\t'.format(b, 5, b * 5), end='')
    print('{}x{}={}\t'.format(c, 5, c * 5), end='')

elif b == c:
    print('{}x{}={}\t'.format(a, 5, a * 5), end='')
    print('{}x{}={}\t'.format(b, 5, b * 5), end='')
    print('{}x{}={}\t'.format(c, 5, c * 5), end='')

else:
    print('Нет 2х равных чисел')

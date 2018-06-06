# Таблица умножения вывод лесницей

for a in range(1, 10):
        for b in range(1,a+1):
            print('{}x{}={}\t'.format(a, b, a * b), end='')
        print()
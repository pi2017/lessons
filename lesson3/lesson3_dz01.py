# Решение домашних задачи 1


def my_len(x):
    counter = 0
    for i in x:
        counter += 1
    return counter

print('Number of symbols ', my_len('hello'))

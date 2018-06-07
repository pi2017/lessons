# Решение домашней задачи 1
# Написать аналог функции len:

def my_len(x):
    counter = 0
    for i in x:
        counter += 1
    return counter

print('Number of symbols ', my_len('hello'))

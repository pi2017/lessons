# coding=utf-8
# Example code
# задачи для закрепления теории
'''
x<0
0<x<100
x>100
'''

numbers = [12, 12515, -12412]


def f(numbers):
    for i in range (len(numbers)):
        if numbers[i] < 0:
            numbers[i] = 'меньше нуля'
        elif 0 < numbers[i] < 100:
            numbers[i] = 'меньше 100'
        else:
            numbers[i] = 'больше 100'

    return numbers


print(f(numbers))

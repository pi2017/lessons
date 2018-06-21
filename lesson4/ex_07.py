# coding=utf-8
# Example code
# задачи для закрепления теории

numbers = [1, -1, 12, -34, 45, 65, -5]
numbers = [-12, -12, 45, -45, -65, -5, -1]


def f(numbers):
    for i in range(-1, -len(numbers), -1):
        if i == -len(numbers):
            break
        if numbers[i - 1] < 0 and numbers[i] >= 0:
            numbers[i - 1] = numbers[i]

    return numbers


print(f(numbers))

# coding=utf-8
# Example code
# Рекурсия функции

def factorial(n):
    if n <  2:
        return 1
    return n * factorial(n - 1)

print (factorial(7))
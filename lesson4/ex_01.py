# coding=utf-8
# Example code
# Вложеные функции


def outer():
    a = 2

    def inner():
        a = 100
    print('inner ', a)
    print()


    inner()
    print('outer ', a)

outer()
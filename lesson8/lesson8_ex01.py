#
#
# raise - вызов ошибки, создание своей ошибки

'''
class Myexception(Exception):
    pass


raise MyException
'''


def div(a, b):
    try:
        return a / b

    except ZeroDivisionError as e:
        print(e)
        return


div(1 / 4)

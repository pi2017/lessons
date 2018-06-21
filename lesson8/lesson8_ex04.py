#
#
#

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass


def run():
    a = input('a: ')

    try:
        print(div(1 / a))
    except TypeError:
        print('Wrong type')

run()

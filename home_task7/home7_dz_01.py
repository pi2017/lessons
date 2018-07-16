# home_work_07
# Напишите программу калькулятор, реализующую операции (+ - * /)
# программа выдает сообщение в случай некорректных данных и продолжает работу.
#

array = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y
}


def calculate(expr):
    numxChars = ""
    operation = None
    numyChars = ""
    for char in expr:
        if char.isdigit():
            if operation is None:
                numxChars += char
            else:
                numyChars += char
        elif char in array:
            operation = char
        elif char.isspace:
            pass
        else:
            raise Exception("invalid character: " + char)
    return array[operation](int(numxChars), int(numyChars))


while True:
    print (calculate(input("введите : ")))
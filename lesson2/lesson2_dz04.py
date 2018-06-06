# Выводим фигуры из звездочек треугольник, елка, квадрат, ромб

a = int(input('a = '))

# for i in range(a):
# print('*' * i)
# print( )

for j in range(a):  # квадрат
    print('*' * a)

for n in range(a):  # треугольник
    print("*" * n)

print( )

for l in range(a):
    if l < a/2:
        print("*")
    if l > a/2:
        print("***")

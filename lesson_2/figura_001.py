class Triangle():
    def __init__(self, side):
        self.side = side

    def draw(self):
        for i in range(self.side):
            print('* ' * i)


triangle = Triangle(6)
triangle.draw()
print()


class Square():
    def __init__(self, side):
        self.side = side

    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)


square = Square(5)
square.draw()
print()

n = int(input('Ведите сторону ромба '))
k = int(input("Количество ромбов "))
print (((n-1)*" "+"+"+(n-1)*" ")*k)
for i in range (2,n+1):
    print (((n-i)*" "+"+"+((i-2)*2+1)*" "+"+"+(n-i)*" ")*k)
for i1 in range (n-1,1,-1):
    print (((n-i1)*" "+"+"+((i1-2)*2+1)*" "+"+"+(n-i1)*" ")*k)
print (((n-1)*" "+"+"+(n-1)*" ")*k)
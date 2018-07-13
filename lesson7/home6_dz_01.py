# ClassAuto
# HomeTask 06
# Создать класс Автомобиль содержащий информацию: модель, цвет, год_выпуска, стоимость.
# Описать метод __str__.

class Auto():

    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        string = "This is: " + '\n' + self.model + '\n' + self.color + '\n' + self.year + '\n' + self.price
        return string


car1 = Auto('Audi', 'Black', '2005', '$10 000')
car2 = Auto('BMW', 'Blue', '2004', '$12 000')
print(car1)
print()
print(car2)
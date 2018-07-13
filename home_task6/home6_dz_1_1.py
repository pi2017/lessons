# ClassAutosalon
# HomeTask 06
# Создать класс Автосалон содержащий информацию: адрес, имя, список доступных машин.
# Реализовать методы для отображения всех доступных машин, добавления новых машин, покупки машин
# (после покупки машина удаляется из списка


class Auto:

    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        string = "This is: " + '\n' + self.model + '\n' + self.color + '\n' + self.year + '\n' + self.price
        return string


class ShowRoom:

    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.cars = []

    def __str__(self):
        string = "Autosalon : " + '\n' + self.address
        return string

    def add_car(self, car):
        self.cars.append(car)

    def show_all(self):
        for index, car in enumerate(self.cars):
            print(index + 1)
            print('-----------------')
            print(car)
            print('-----------------')
            print()

    def sell_car(self, car):
        if self.cars.__contains__(car):
            self.cars.remove(car)
            print(' Car has bin sold!')
        else:
            print('No such car')


car1 = Auto('Audi', 'Black', '2005', '$10 000')
car2 = Auto('BMW', 'Blue', '2004', '$12 000')

showroom = ShowRoom('Borispolska, 5', 'SaleCar')

showroom.add_car(car1)
showroom.add_car(car2)
showroom.show_all()

showroom.sell_car(car1)
showroom.show_all()

print('-----------------')
print(showroom)

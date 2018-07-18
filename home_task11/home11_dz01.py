"""
задача 1
Написать функцию-генератор генерирующую данные о людях.
Пример:
>>for person in gen_person():
	print(person)
[‘Alex’, ‘Smith’, 23]
[‘Bob’ , ‘Alan’, 44]
..
Создать класс Person содержащий поля имя, фамилия, возраст
Сгенерировать список из 100 экземпляров класса Person
[Person(‘Alex’, ‘Smith’, 23), Person(‘Bob’, ‘Alan’, 44)…]
Найти самого старшего и самого младшего человека из списка.
Вывести результат на экран.
"""


# name_abc = ('Andrey', 'Savor', '22','Bob', 'Skvoh', '19', 'Sergey', 'Moryak', '40')


def gen_person():
    mylist = ['Andrey', 'Savor', '22', 'Bob', 'Skvoh', '19', 'Sergey', 'Moryak', '40']

    for i in mylist:

        return i


mygen = gen_person()
print(mygen)

for i in mygen:
    print(i)

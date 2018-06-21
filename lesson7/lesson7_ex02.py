#
#
# USERS CLASS
class Person:
    pass

    def __init__(self, name, age):
        self.name = name
        self.age = age


alex = Person('Alex', 20)
kate = Person('Kate', 22)

# alex = Person()
# alex.name = 'Alex'
# alex.age = 20

# kate = Person()
# kate.name = 'Kate'
# kate.age = 24

print(alex.name, alex.age)
print(kate.name, kate.age)

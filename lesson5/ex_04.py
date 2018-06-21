users = [
    ['grom', 30],
    ['ant', 21],
]

for i in enumerate(users):
    print(i, users)

print(end='\n')

a = [1, 2, 3]
b = [5, 6, 7, *a]

print(b)

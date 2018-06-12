# Задача 4
# Заменить элементы с нечетными номерами на 0
# 	[1, 1, 1, 1, 1] -> [1, 0, 1, 0, 1]

numbers = [1, 1, 1, 1, 1]
print(numbers, end='\n\n')
for i in range(len(numbers) - 1):
    if i % 2 == 1:
        numbers[i] = 0

print(numbers)

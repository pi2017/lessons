# Задача 2
# Заменить каждый элемент на следующий, последний на первый
# 	[1, 2, 3, 4] -> [2, 3, 4, 2]

numbers = [1, 2, 3, 4]

for i in range(len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers[len(numbers) - 1] = numbers[0]

print(numbers)

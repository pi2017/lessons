# Задача 1
# Дан список чисел, заменить каждый отрицательный элемент на следующий
# 	[1, 2, -3, 5, -6, 7, -9] -> [1, 2, 5, 5, 7, 7, -9]

numbers = [1, 2, -3, 5, -6, 7, -9]

for i in range(len(numbers) - 1):
    if numbers[i] < 0:
        numbers[i] = numbers[i + 1]

        print(numbers, end='\n\n')

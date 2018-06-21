# Задача 5
# Посчитать сумму первых двух четных чисел в списке
# 	[5, 7, 8, 3, 4, 6, 8] -> 12

data = [5, 7, 8, 3, 4, 6, 8]
result: int = 0
amount_even: int = 0

print(data, end='\n\n')

for i in range(len(data) - 1):
    if data[i] % 2 == 0:
        amount_even += 1
        result += data[i]

        if amount_even == 2:
            break

print('Сумма 2х четных = ', result)

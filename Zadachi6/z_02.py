#
# найти сумму положительных элементов

my_lst = [-2, -31, 56, 78, -23]

for i in range(len(my_lst)):
    number = 0
    sum = 0

    if my_lst[i] > 0:
        number += 1
        sum += my_lst[i]

        print('Сумма положительных :) ', sum)

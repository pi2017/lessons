#
# Дан список отрицательных и положительных чисел, заменить все элементы
# на противоположные по знаку


my_lst = [-12, -31, -56, 78, -24]
print(my_lst)

for i in range(len(my_lst)):

    if  my_lst[i] < 0:
        my_lst[i] = my_lst[i] * (-1)
    else:
        my_lst[i] = my_lst[i] * (-1)
print(my_lst)

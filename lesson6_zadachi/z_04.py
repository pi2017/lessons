#
# найти в списке максимум и минимум и поменять местами

my_lst = [-12, -31, -56, 78, -24]

i = 0
ind_min = 0
ind_max = 0
min = my_lst[i]
max = my_lst[i]
while i < len(my_lst):
    if my_lst[i] < min:
        min = i
        min = my_lst[i]
        ind_min = i
    if my_lst[i] > max:
        max = i
        max = my_lst[i]
        ind_max = i
    i = i + 1
my_lst[ind_max], my_lst[ind_min] = my_lst[ind_min], my_lst[ind_max]

print('Минимум ', ind_min, min, 'Максимум ', ind_max, max)
print(my_lst)

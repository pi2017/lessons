# Zadacha 04

name = input('введите имя до 13 символов ')
separator = '-'
konst = 15

full_name = separator + name + separator  # склеивание строк

len_name = len(full_name)  # длинна строки

line_1 = '-' * konst  # повторение строки

print(line_1)
print("{0:<1}{1:^13}{2:>1}".format(separator, name, separator))
print(line_1)

f_name = input('Введите фамилия студента ')
name = input('Введите имя студента ')
o_name = input('Введите отчество студента ')
group_st = input('Введите номер группы студента ')

konst = 1
separator = "*"

data_group_1 = len(separator + f_name + name + o_name + separator)
data_group_2 = len(separator + 'Выполнил студент(ка) группы № '+ group_st + separator)


if data_group_1 > data_group_2:
            line = data_group_1 * "*" + "*"
else:
            line = data_group_2 * "*" + "*"
print(line)
print("{0:<1}{1:<1}{2:>2}".format(separator, 'Лабораторная работа № 1', separator))
print("{0:<1}{1:<1}{2:<1}{3:>2}".format(separator, 'Выполнил студент(ка) группы № ', group_st, separator))
print("{0:<1}{1:<1} {2:<1} {3:<1}{4:>2}".format(separator, f_name, name, o_name, separator))
print(line)

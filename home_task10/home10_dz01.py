"""
задача 1
Переписать информацию с одного файла в другой
"""

with open(r'output.txt', 'w') as output, open('input.txt', 'r') as input:
    output.write(input.read())

output.close()
input.close()
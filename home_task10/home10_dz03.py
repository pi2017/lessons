"""
задача 3
Определите размер файла имя которого вводит пользователь.
Выведите его на экран.
Выведите его в байтах, мегабайтах, гигабайтах.
"""

import os

cwd = os.getcwd()
print(cwd)

file_path = input("Введите путь к файлу: ")
if os.path.exists(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(r'input.txt')
        print(os.path.getsize(r'input.txt'), 'Byte')
        ksize = size//1024
        print(ksize,'Kbyte')
    else:
        print('Destination path does not exist')
else:
    print('File does not exist')

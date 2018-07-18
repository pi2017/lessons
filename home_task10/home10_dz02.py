"""
задача 2
Скопировать файл в выбранную директорию.
Пример:
Введите путь к файлу:
>>files/avatar.jpg
Куда скопировать?
>>files2/
Готово!
"""

import os
import shutil

cwd = os.getcwd()
print(cwd)

file_path = input("Введите путь к файлу: ")
if os.path.exists(file_path):
    file_dest = input('Куда скопировать?: ')
    if os.path.exists(file_dest):
        shutil.copy2(r'input.txt', file_dest)
        print('File was copied')
    else:
        print('Destination path does not exist')
else:
    print('File does not exist')



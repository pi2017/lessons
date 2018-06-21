# Найти номер и значение первого положительного элемента списка
#

def even_number(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            return i, arr[i]


if __name__ == '__main__':
    result = [-12, 3, -4, 7, 90]
    print(even_number(result))

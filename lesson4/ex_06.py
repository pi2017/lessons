# coding=utf-8
# Example code
# задачи для закрепления теории

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1, i, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

    return numbers

print(bubble_sort([4, 8, 3, 1, 5, 7, 2]))
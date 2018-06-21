# coding=utf-8
# Example code
# задачи для закрепления теории

def mean_func(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

n = mean_func([1,2,3,4,5])
print ('Mean number = ', n)


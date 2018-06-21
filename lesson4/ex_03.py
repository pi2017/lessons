# coding=utf-8
# Example code
# Число Фибоначи

def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Fibonache = ', fib(12))

if __name__ == "__main__":
    print('Fibonache = ', fib(13))

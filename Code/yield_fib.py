#!/usr/bin/env python3

def fib(n):
    current = 0
    a, b = 1, 1
    while current < n:
        yield a
        a, b = b, a+b
        current += 1

f5 = fib(5)
print(f5)

for i in f5:
    print(i)

#!/usr/bin/env python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Əsas hissə
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except:
        print(0)
else:
    print(0)

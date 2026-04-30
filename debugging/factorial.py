#!/usr/bin/env python3
import sys

def factorial(n):
    try:
        n = int(n)
        if n <= 1:
            return 1
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    except:
        return 1   

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(factorial(sys.argv[1]))
    else:
        print(1)

#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.
    
    Parameters:
    n (int): A non-negative integer whose factorial needs to be calculated.
    
    Returns:
    int: The factorial value of the input number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)

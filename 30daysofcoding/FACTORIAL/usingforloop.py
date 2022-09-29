import math
import os
import random
import re
import sys


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

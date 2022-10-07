
import math
import os
import random
import re
import sys

def pairs(k, arr):
    arr=set(arr)
    
    res=0
    for i in arr:
        x= i-k
        if x in arr:
            res+=1
    
    return res
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

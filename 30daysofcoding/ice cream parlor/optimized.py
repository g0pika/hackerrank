

import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    map1 = {}
    for i, num in enumerate(arr):
        diff = m - num
        if num in map1:
            return map1[num], i + 1
        else:
            map1[diff] = i + 1        
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

import math
import os
import random
import re
import sys

def bitwiseAnd(N, K):
    res = 0
    s = []
    
    for i in range(1, N+1):
        for j in range(1,i):
            bit = i & j
            if res == K-1:
                return res
            
            if bit < K and res < bit:
                res = bit
                
    return res
    
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()

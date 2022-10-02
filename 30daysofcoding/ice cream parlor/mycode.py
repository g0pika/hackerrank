

import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == m:
                return i+1, j+1
              
#This code will have a time complexity of O(n^2). 
#So let's move on to the next approach using hashmap.               
    
            
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

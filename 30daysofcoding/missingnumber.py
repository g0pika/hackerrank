
import math
import os
import random
import re
import sys
from collections import Counter

def missingNumbers(arr, brr):
    missing = []
    for i in brr:
        if i in arr:
            arr.remove(i)
        else: 
          #Only include a missing number once, even if it is missing multiple times.
            if i not in missing:
                missing.append(i)
    
    return sorted(missing)
                         
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

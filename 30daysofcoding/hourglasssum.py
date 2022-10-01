

import math
import os
import random
import re
import sys
            
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        A = arr.append(list(map(int, input().rstrip().split())))
    
mx = -63
for i in range(6):
    for j in range(6):
        if 0<i<5 and 0<j<5:
            res = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if res > mx:
                mx = res
    
print(mx)
    

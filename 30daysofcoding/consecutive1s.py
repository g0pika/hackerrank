
import math
import os
import random
import re
import sys

def binarynumbers(n):
    
    binary = []
    while n>0:
        remainder = n%2
        n = int(n/2)
        binary.append(remainder)
    
    count = 0
    mx = 0
    for i in binary:
        if i == 1:
            count +=1
            if mx < count:
                mx = count
        else:
            count = 0   
    return mx        
    

if __name__ == '__main__':
    n = int(input().strip())

print(binarynumbers(n))
     

            


import math
import os
import random
import re
import sys


def superReducedString(s):
    
    while True:
        flag = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                flag = 1
                break
        
        if flag == 0:
            break
    
    if len(s)== 0:
        return 'Empty String'
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

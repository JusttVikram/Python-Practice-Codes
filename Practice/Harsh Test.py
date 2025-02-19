import re
import sys
import math
import random
import os


def solve(ar):
    result = []
    
    for s in ar:
        modified = [s[0]]
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                modified.append(s[i])
        
        result.append(''.join(modified))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
    fptr.write("\n")
    
    ar_count = int(input().strip())
    arItems = input().rstrip().split(" ")
    
    ar = []
    for i in range(ar_count):
        ar_item = arItems[i]
        ar.append(ar_item)
    
    outcome = solve(ar)
    
    for i in range(len(outcome)):
        fptr.write(str(outcome[i]))
        if i < len(outcome)-1:
            fptr.write(" ")
    fptr.write("\n")
    
    fptr.close()

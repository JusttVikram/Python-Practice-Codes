# Leetcode 476 

def findComplement(num):
    i = 1
    while i <= num:
        i = i << 1
    return (i - 1) ^ num
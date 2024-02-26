def calcsum(a,b):
    s = a+b
    return s

def calcavg(a,b,c):
    avg = (a+b+c)/3
    return avg

def lengthoflist(list):
    return(len(list))

def printinsingleline(list):
    for item in list:
        print(item, end= " ")

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def USD_to_INR(n):
    return float(82.85*n) # 1 USD = 82.85 INR

def Odd_or_Even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
"""Recursion"""

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

def sum_of_first_n_natural_numbers(n):
    
    if n==0:
        return 0
    return sum_of_first_n_natural_numbers(n-1) + n

def print_list(list, index=0):
    if index == len(list):
        return
    print(list[index])
    print_list(list, index+1)

l1 = [1,3,4,'a','b']

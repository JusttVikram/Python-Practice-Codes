"""Using recursion"""

def factorial_using_recursion(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_using_recursion(num-1)


"""Without using recursion"""

def factorial_without_using_recursion(num):
    result = 1
    for i in range(1,num+1):
        result *=i
    return result


num = int(input("Enter a positive number : "))
print(factorial_using_recursion(num))
print(factorial_without_using_recursion(num))
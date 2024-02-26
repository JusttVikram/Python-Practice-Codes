n = int(input("Enter a number : "))
sum = 0

"""Using While Loop"""
# while n >= 0:
#     sum = sum + n
#     n = n-1

# print(sum)


"""Using For Loop"""

for i in range(1, n+1):
    sum += i
print(sum)
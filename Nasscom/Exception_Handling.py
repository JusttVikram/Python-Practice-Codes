a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

try:
    c = a/b
    print("result : ", c)
except:
    print("Cannot divided by zero. Please try again..!!")

# Else is not mandatory to use.
else:
    print("Continue.")

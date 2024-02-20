a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")


if a>=b and b>=c:
    # print(a + " is largest.")
    print(f"{a} is largest.")
elif b>=a and a>=c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")
squares = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("Enter a number in between 1 and 10 : "))
x = 49

i = 0

while i < len(squares):
    if squares[i] == x :
        print(True, i)
    else:
        print(False)
    i+=1

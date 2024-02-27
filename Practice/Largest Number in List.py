a = []
Length = int(input("Enter the length of list : "))

for i in range(Length):
    value = int(input("Enter the value: "))
    a.append(value)

max = a[0]
for i in range(Length):
    if a[i] > max:
        max = a[i]

print(f"{a[i]} is max.")

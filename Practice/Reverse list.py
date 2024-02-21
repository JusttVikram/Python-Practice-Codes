# a = [12, 15, 17, 19, 23, 27]
# start = 0
# end = len(a) - 1

# while start < end:
#     a[start], a[end] = a[end], a[start]
#     start += 1
#     end -= 1

# print(a)



a = [12, 15, 17, 19, 23, 27]
start = 0
end = len(a) - 1

for i in range(len(a)):

    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1

print(a)
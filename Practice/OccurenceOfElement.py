def count(list,x):
    count = 0
    for i in list:
        if i==x:
            count = count +1

    return count

list =[1,1,1,2,2,4,5,6,8,65,0]
x= 34

print(f"{x} has {count(list,x)} occurences.")
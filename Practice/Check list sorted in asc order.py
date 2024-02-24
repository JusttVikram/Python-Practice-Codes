def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

lst=[3,2,4,6,8]
list = [1,2,3,4,6]
print(is_sorted(lst))
print(is_sorted(list))
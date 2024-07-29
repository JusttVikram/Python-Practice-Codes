# Write a Python program to merge two sorted lists into a single sorted list.

def merge_sorted_list(list1, list2):
    return sorted(list1 + list2)

list1 = [1, 2, 3, 4, 5]
list2= [6, 7, 8, 9, 10]

print(merge_sorted_list(list1, list2))
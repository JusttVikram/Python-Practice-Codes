def sort_list_asc(lst):
    lst.sort()
    return lst

def sort_list_dsc(lst):
    lst.sort(reverse = True)
    return lst

# Example usage
my_list = [5, 2, 9, 1, 7]

sorted_list_asc = sort_list_asc(my_list)
print(sorted_list_asc)

sorted_list_dsc = sort_list_dsc(my_list)
print(sorted_list_dsc)
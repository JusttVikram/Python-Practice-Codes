# Implement a function to find the mode of a list of numbers.

def mode(list):
    return max(set(list), key = list.count)


list = [22,88,33,44,55]
print(mode(list))
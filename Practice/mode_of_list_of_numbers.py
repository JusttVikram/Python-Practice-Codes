# Implement a function to find the mode of a list of numbers.

'''The max function in Python is a built-in function that returns the maximum value from a sequence or a set of arguments. In this case, the max function is called with two arguments: set(list) and key=list.count.

The set(list) part converts the given list into a set, which removes any duplicate elements. This is done to ensure that each element is counted only once when determining the most frequent element.

The key=list.count part specifies a function that is used to determine the sorting order. In this case, the list.count function is used as the key function. The list.count function returns the number of occurrences of a given element in the list. By using this key function, the max function will compare the elements based on their count in the list and return the element with the highest count.

Overall, this function implementation finds the most frequent element in a given list by converting the list into a set to remove duplicates and using the max function with a key function that counts the occurrences of each element.'''

def mode(list):
    return max(set(list), key = list.count)


list = [22,88,33,44,55]
print(mode(list))


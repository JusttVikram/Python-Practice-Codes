#  Implement a function to find the maximum subarray sum in a given list.

def max_subarray_sum(arr):

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num )
        max_sum = max(current_sum, max_sum)

    return max_sum


print(max_subarray_sum([1,3,4,5]))
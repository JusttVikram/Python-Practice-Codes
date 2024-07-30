# Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

def PalinArray(arr):
    for i in range(len(arr)):
        if str(arr[i]) != str(arr[i])[::-1]:
            return False
    return True
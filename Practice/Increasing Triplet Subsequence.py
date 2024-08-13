# Leetcode 334

def increasingTriplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

#test case

print(increasingTriplet([1,2,3,4,5])) #True
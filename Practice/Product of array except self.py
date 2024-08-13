def productExceptSelf(nums):
    n = len(nums)
    res = [1]*n
    left = 1
    right = 1
    for i in range(n):
        res[i] *= left
        left *= nums[i]
        res[~i] *= right
        right *= nums[~i]
    return res


nums = [1,2,3,4]
print(productExceptSelf(nums)) # [24,12,8,6]
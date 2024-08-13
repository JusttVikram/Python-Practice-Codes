# Leetcode 238

def productExceptSelf(self, nums: List[int]) -> List[int]:
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
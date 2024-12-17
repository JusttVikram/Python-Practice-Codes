# Leetcode 1822
from typing import List 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        count = 0
        for i in nums:
            if i < 0:
                count += 1
        if count % 2 == 0:
            return 1
        else:
            return -1
# Leetcode 1679

from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res, d = 0, Counter(nums)
        for val1, val1_cnt in d.items():
            val2 = k - val1
            if val1 < val2 or val2 not in d:
                continue 
            res += min(val1_cnt, d[val2]) if val1 != val2 else val1_cnt // 2
        
        return res

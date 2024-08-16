#  Leetcode 1732.
from typing import List

def largestAltitude(self, gain : List[int]) -> int:
    max = 0
    current = 0
    for i in gain:
        current += i
        if current > max:
            max = current
    return max
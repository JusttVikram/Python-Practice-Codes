# Leetcode 1491
from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)

# Leetcode 2352

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row = [0]*n
        col = [0]*n
        for i in range(n):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        ans = 0
        for i in range(n):
            for j in range(n):
                if row[i] == col[j]:
                    ans += 1
        return ans
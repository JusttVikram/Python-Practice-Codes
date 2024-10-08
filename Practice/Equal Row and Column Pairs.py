# Leetcode 2352

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        out = 0
        n = len(grid)
        for i in range(n):
            row = ",".join(map(str,grid[i]))
            for j in range(n):
                col = ','.join(str(grid[k][j]) for k in range(n))
                if row == col:
                    out += 1
        return out

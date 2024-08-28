# Leetcode 1905.

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid2) or j >= len(grid2[0]) or grid2[i][j] == 0:
                return 1
            grid2[i][j] = 0
            res = grid1[i][j]
            res &= dfs(i+1, j)
            res &= dfs(i-1, j)
            res &= dfs(i, j+1)
            res &= dfs(i, j-1)
            return res
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    count += dfs(i, j)
        return count
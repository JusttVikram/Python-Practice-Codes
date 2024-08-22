#Leetcode 1937

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        dp = [[0]*m for _ in range(n)]
        for j in range(m):
            dp[0][j] = points[0][j]
        for i in range(1, n):
            left = [0]*m
            right = [0]*m
            left[0] = dp[i-1][0]
            for j in range(1, m):
                left[j] = max(left[j-1]-1, dp[i-1][j])
            right[m-1] = dp[i-1][m-1]
            for j in range(m-2, -1, -1):
                right[j] = max(right[j+1]-1, dp[i-1][j])
            for j in range(m):
                dp[i][j] = max(left[j], right[j], dp[i-1][j]) + points[i][j]
        return max(dp[-1])
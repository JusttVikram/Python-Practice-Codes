# Leetcode 539

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        min_diff = float('inf')
        for i in range(1, len(timePoints)):
            diff = self.time_diff(timePoints[i], timePoints[i-1])
            min_diff = min(min_diff, diff)
        diff = self.time_diff(timePoints[0], timePoints[-1])
        min_diff = min(min_diff, diff)
        return min_diff
    
    def time_diff(self, time1, time2):
        h1, m1 = map(int, time1.split(':'))
        h2, m2 = map(int, time2.split(':'))
        diff = (h1-h2)*60 + m1-m2
        return min(abs(diff), 1440-abs(diff))
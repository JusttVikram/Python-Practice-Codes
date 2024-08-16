# Leetcode 624.

# My solution

from typing import List

def maxDistance(arrays: List[List[int]]) -> int:
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    result = 0
    for i in range(1, len(arrays)):
        result = max(result, max(abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])))
        min_val = min(min_val, arrays[i][0])
        max_val = max(max_val, arrays[i][-1])
    return result


# Someones else's solution


class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
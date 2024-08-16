#  Leetcode 1732.

def largestAltitude(self, gain : List[int]) -> int:
    max = 0
    current = 0
    for i in gain:
        current += i
        if current > max:
            max = current
    return max
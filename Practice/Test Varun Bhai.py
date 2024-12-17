# Given an array a of positive integers, find the number of pairs of integers for which the difference of the two numbers is equal to a number k. Since the number of pairs could be quite large, take modulo 10**9+7 for output.

def solution(k, a):
    freq = {}
    count = 0
    for num in a:
        if num - k in freq:
            count += freq[num - k]
        if num + k in freq:
            count += freq[num + k]
        freq[num] = freq.get(num, 0) + 1
    return count % (10**9 + 7)


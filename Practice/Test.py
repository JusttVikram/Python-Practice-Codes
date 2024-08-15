# Given an array a of positive integers, find the number of pairs of integers for which the difference of the two numbers is equal to a number k. Since the number of pairs could be quite large, take modulo 10**9+7 for output.

def solution(k, a):
    a.sort()
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] - a[i] == k:
                count += 1
    return count % (10**9 + 7)
# Given a string s, extract all the integers from s.


def extractIntegers(s):
    return [int(i) for i in s.split() if i.isdigit()]

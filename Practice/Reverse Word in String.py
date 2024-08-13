# Leetcode 151. Reverse Words in a String


def reverseWords(s : str):
    return " ".join(s.split()[::-1])



print(reverseWords("the sky is blue")) # "blue is sky the"
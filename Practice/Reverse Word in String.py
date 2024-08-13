# Leetcode 151. Reverse Words in a String

def reverseWords(self,s: str) -> str:
    return " ".join(s.split()[::-1])
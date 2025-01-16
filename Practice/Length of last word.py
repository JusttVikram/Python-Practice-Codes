#Leetcode 58

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing whitespace
        s = s.strip()
        
        # If string is empty after stripping, return 0
        if len(s) == 0:
            return 0
            
        # Split string into list of words
        s = s.split()
        
        # Return length of last word
        return len(s[-1])
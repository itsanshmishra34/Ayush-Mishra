class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])
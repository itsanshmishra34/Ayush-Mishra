class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        return a == a[::-1]
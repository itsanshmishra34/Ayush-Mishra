class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = bin(n)
        c = 0
        for i in str(a):
            if i=='1':
                c+=1
        return c
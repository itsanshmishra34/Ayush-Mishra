class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        e = int(a,2)
        f = int(b,2)
        return bin(e+f)[2:]  
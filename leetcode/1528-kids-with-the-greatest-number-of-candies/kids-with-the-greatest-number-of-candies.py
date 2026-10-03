class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a = []
        for i in candies:
                a.append(int(i)+extraCandies>=max(candies))
        return a
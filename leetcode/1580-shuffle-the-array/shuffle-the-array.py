class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a = []
        c = []
        d = []
        b = len(nums)//2
        for i in range(b):
            a.append(nums[i])
        for j in range(b,len(nums)):
            c.append(nums[j])
        for i in range(b):
            d.append(a[i])
            d.append(c[i])
        return d
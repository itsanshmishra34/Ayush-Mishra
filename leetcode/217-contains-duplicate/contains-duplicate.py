class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        b = set()
        for i in nums:
            if i in b:
                return True
            else:
                b.add(i)
        return False
            
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mean = nums[len(nums)//2]
        return sum(abs(mean-i) for i in nums)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = []
        for i in range(m):
            a.append(nums1[i])
        for j in range(n):
            a.append(nums2[j])
        a.sort()
        nums1[:] = a
        return a
        
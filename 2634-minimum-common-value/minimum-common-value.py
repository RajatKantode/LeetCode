class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s=set(nums1)
        
        for i in nums2:
            if i in s:
                return i
        return -1
        
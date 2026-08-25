class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=1
        while True:
            if k*c not in nums:
                return k*c
            else:
                c+=1
        
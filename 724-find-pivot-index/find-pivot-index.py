class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=sum(nums)
        l=0

        for i in range(len(nums)):
            r=t-l-nums[i]

            if r==l:
                return i
            l+=nums[i]
        return -1        
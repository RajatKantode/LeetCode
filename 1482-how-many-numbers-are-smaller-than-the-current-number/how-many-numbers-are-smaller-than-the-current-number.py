class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_n=sorted(nums)
        l=[]
        for i in nums:
            l.append(sort_n.index(i))
        return l
        
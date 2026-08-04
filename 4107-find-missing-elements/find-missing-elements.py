class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        s=set(nums)
        res=[]
        for i in range(min(nums),max(nums)+1):
            if i not in s:
                res.append(i)
        return res
        
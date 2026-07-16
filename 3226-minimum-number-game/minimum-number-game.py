class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l=[]
        for i in range(0,len(nums),2):
            l.append(nums[i+1])
            l.append(nums[i])
        return l
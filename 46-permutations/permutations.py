class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
   
        if len(nums)==0:
            return [[]]
        l=[]
        for i in range(len(nums)):
            c=nums[i]
            rem=nums[:i]+nums[i+1:]

            for p in self.permute(rem):
                l.append([c]+p)
        return l
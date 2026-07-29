class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()

        left,right=0,len(nums)-1
        ans=float('inf')

        while left<right:
            avg=(nums[left]+nums[right])/2.0
            ans=min(ans,avg)
            left+=1
            right-=1
        return ans
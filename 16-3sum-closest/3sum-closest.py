class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        close_sum=float('inf')
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,h=i+1,n-1
            while l<h:
                c_sum=nums[i]+nums[l]+nums[h]

                if abs(c_sum-target)<abs(close_sum-target):
                    close_sum=c_sum
                
                if c_sum==target:
                    return c_sum
                elif c_sum<target:
                    l+=1
                else:
                    h-=1   
        return close_sum
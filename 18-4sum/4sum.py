class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        key=[]
        for i in range(n):
        
            if i>0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                h=n-1
                while l<h:
                    res=nums[i]+nums[j]+nums[l]+nums[h]
                    if res==target:
                        key.append([nums[i],nums[j],nums[l],nums[h]])
                        l+=1
                        h-=1
                        while l<h and nums[l]==nums[l-1]:
                            l+=1
                        while l<h and nums[h]==nums[h+1]:
                            h-=1
    
                    elif res< target:
                        l+=1
                    else :
                        h-=1
        return key

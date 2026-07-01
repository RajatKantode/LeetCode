class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # c=1
        # n = len(nums) // 2

        # if len(nums) == 1:
        #     return nums[0]

        # for i in range(len(nums)):
        #     if i>0 and nums[i-1]==nums[i]:
        #         c+=1
        #         if c>n:
        #             return nums[i]
        #     else:
        #         c=1

        c=0
        n=None
        for i in nums:
            if c==0:
                n=i
            c+= 1 if i==n else -1
        return n
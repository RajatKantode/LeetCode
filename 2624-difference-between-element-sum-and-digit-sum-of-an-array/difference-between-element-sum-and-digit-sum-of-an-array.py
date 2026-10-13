class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e_sum=sum(nums)
        d_sum=0

        for num in nums:
            while num>0:
                d_sum+=num%10
                num//=10

        return abs(e_sum-d_sum)
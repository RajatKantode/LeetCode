class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                res=(nums[i]-1)*(nums[j]-1)
                if res>max_product:
                    max_product=res
        return max_product

        
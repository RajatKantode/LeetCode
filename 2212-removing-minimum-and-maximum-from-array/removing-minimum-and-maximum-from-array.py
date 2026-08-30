class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        l = min(min_i, max_i)
        r = max(min_i, max_i)

        return min(r + 1,n - l,l + 1 + n - r )
        
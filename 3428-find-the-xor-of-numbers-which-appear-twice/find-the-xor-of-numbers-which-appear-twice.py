class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        res = 0

        for i in nums:
            if i in s:
                res ^= i
            else:
                s.add(i)

        return res
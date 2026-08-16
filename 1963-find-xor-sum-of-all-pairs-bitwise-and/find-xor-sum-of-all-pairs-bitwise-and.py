class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        x1 = 0
        for x in arr1:
            x1 ^= x

        x2 = 0
        for x in arr2:
            x2 ^= x

        return x1 & x2       
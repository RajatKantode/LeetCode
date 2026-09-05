class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}

        for i in nums:
            d[i]=d.get(i,0)+1

        res=0
        for i,j in d.items():
            if j==1:
                res+=i

        return res
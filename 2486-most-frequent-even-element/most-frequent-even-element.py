class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i%2==0:
                d[i]=d.get(i,0)+1
        if len(d)==0:
            return -1
        m=max(d.values())
        return min(i for i, j in d.items() if j == m) 
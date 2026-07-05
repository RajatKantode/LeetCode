class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        for i,j in d.items():
            if j==2:
                l.append(i)
        return l
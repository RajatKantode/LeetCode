class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        
        l=list(d.keys())

        l.sort(key=lambda i:d[i],reverse=True)
        return l[:k]
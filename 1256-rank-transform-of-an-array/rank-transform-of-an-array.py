class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s=sorted(set(arr))
        r={}
        for i, j in enumerate(s):
            r[j]=i+1
        return [r[i] for i in arr]
class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        d={}
        while n:
            a=n%10
            d[a]=d.get(a,0)+1
            n//=10
        res=0
        for i,j in d.items():
            res+=i*j
        return res
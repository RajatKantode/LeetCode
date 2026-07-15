class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s=n*(n+1)/2
        
        ds=0
        for i in range(1,n+1):
            if i%m!=0:
                ds+=i
        return ds-(s-ds)
        
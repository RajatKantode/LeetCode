class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        p=1000
        while n>=p:
            c+=n-p+1
            p*=1000
        return c
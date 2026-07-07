class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        n=n.replace('0','')
        if not n:
            return 0
        c=0
        for i in n:
            c+=int(i)
        return int(n)*c
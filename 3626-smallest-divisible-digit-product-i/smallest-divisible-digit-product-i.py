class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            x=n
            prod=1

            while x:
                d=x%10
                if d==0:
                    prod=0
                    break
                prod*=d
                x//=10
            if prod%t==0:
                return n
            n+=1
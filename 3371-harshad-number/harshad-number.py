class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        c=0
        a=x
        while a:
            d=a%10
            c+=d
            a//=10
        if x%c==0:
            return c
        else:
            return -1
            

        
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        rem = 1
        org = n

        while n != 0:
            sum = sum + n % 10
            rem = rem * (n % 10)
            n = n // 10

        result = sum + rem

        if org % result == 0:
            return True
        else:
            return False
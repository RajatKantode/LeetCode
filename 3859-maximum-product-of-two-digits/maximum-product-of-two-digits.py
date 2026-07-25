class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = -1
        second = -1

        while n:
            digit = n % 10

            if digit > first:
                second = first
                first = digit
            elif digit > second:
                second = digit

            n //= 10

        return first * second
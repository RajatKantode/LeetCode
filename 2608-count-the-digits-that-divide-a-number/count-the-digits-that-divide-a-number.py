class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        original = num
        count = 0

        while num > 0:
            digit = num % 10
            if original % digit == 0:
                count += 1
            num //= 10

        return count
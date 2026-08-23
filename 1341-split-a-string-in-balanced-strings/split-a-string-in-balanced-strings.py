class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        bal = 0
        c = 0

        for i in s:
            if i == 'L':
                bal += 1
            else:
                bal -= 1

            if bal == 0:
                c += 1

        return c
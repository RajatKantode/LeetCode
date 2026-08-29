class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        y=s.split("|")
        return sum(i.count("*")for i in y[::2])

        
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i, ch in enumerate(s, 1):
            reverse_value = ord('z') - ord(ch) + 1
            total += i * reverse_value

        return total
        
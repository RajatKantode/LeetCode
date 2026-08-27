class Solution(object):
    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        
        count = 0
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i + 1] == '1':
                count += 1
        
        return count == 1
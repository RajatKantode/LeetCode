class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0

        for i in range(1,len(s)):
            if s[i].lower()!=s[i-1].lower():
                c+=1

        return c
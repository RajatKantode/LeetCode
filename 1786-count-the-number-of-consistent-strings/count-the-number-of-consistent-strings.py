class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allow=set(allowed)
        res=0
        
        for i in words:
            for j in i:
                if j not in allow:
                    break
            else:
                res+=1
        return res
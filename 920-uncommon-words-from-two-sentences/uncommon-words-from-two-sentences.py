class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        freq = {}
        sen = (s1 + " " + s2).split()

        for i in sen:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        result = []

        for i in freq:
            if freq[i] == 1:
                result.append(i)

        return result
        
        
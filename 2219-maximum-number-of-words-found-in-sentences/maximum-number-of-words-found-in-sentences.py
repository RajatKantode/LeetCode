class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m=0
        for i in sentences:
            word=len(i.split())
            if word>m:
                m=word
        return m
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        ans = [first]
        for e in encoded:
            ans.append(ans[-1] ^ e)
        return ans
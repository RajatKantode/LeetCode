class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        res=min(x,y//4)

        if res%2==1:
            return "Alice"
        else:
            return "Bob"        
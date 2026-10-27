class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid=[]

        for i in range(m):
            row=['#']*n
            grid.append(row)

        for j in range(n):
            grid[0][j]= '.'

        for i in range(m):
            grid[i][n-1]= '.'

        return [''.join(row) for row in grid]
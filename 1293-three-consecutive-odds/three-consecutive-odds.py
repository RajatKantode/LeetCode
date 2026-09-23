class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0

        for num in arr:
            if num%2==1:  
                c+=1

                if c==3:
                    return True
            else:
                c=0  

        return False
        
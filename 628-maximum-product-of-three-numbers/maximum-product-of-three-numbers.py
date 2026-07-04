class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=m2=m3=float('-inf')
        n1=n2=float('inf')

        for i in nums:
            if i>m1:
                m3=m2
                m2=m1
                m1=i
            elif i>m2:
                m3=m2
                m2=i
            elif i>m3:
                m3=i
            
            if i<n1:
                n2=n1
                n1=i
            elif i<n2:
                n2=i
        return max(m1*m2*m3,m1*n1*n2)
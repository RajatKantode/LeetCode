class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        ans=[]
        for i in nums1:
            d[i]=d.get(i,0)+1
        
        for i in nums2:
            if d.get(i,0)>0:
                ans.append(i)
                d[i]-=1
        return ans

        
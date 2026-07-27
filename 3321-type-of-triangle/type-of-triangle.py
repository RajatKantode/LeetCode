class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a,b,c=nums[0],nums[1],nums[2]
        if len(nums)<3:
            return "none"
        valid=(a+b>c) and (a+c>b) and (b+c>a)
        if not valid:
            return "none"
        if a==b==c:
            return "equilateral"    
        elif a==b or b==c or a==c:
            return "isosceles"
        else:
            return "scalene"
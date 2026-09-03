class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        odd = [x for x in nums1 if x % 2!=0]
        even = [x for x in nums1 if x % 2 == 0]

        if not odd:
            return True

        if not even:
            return True

        return min(odd) < min(even)
        
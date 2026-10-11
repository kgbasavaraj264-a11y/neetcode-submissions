class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dp=[]
        for i in nums1:
            if i in (nums2) and (i not in dp):
                dp.append(i)
        return dp
       
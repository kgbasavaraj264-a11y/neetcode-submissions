class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        n=len(nums1)
        if n%2!=0:
            mid=nums1[n//2]
        else:
            m1=nums1[n//2]
            m2=nums1[(n-1)//2]
            mid=(m1+m2)/2

        return mid        
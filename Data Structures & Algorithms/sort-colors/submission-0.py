class Solution:
    def sortColors(self, n: List[int]) -> None:
        i=0
        mid=0
        j=len(n)-1
        while(mid<=j):
            if n[mid]==0:
                n[i],n[mid]=n[mid],n[i]
                i=i+1
                mid=mid+1
            elif n[mid]==1:
                mid=mid+1
            else:
                n[mid],n[j]=n[j],n[mid]
                j=j-1

        """
        Do not return anything, modify nums in-place instead.
        """
        
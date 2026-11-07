class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}
        x=0
        for i in nums:
            if i in h.keys():
                x=h[i]
                x=x+1
                h[i]=x
            else:
                h[i]=1
        a=max(h,key=h.get)
        return a
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i in h.keys():
                x=h[i]
                x=x+1
                h[i]=x
            else:
                h[i]=1

        for key in list(h):
            if h[key]>1:
                del h[key]
        for key in h:
            return key       
                
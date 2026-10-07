class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        x=1
        count=0
        for i in nums:
            if i in h.keys():
                count=count+1 
            else:
                h[i]=x
            x=x+1
        if count>=1:
            return True 
        else:
            return False

        
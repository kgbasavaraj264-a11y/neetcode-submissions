class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=0
        b=[]
        for i in digits:
            x=x*10
            x=x+i
        x=x+1
        while(x!=0):
            r=x%10
            x=x//10
            b.append(r)
        return b[::-1]
        
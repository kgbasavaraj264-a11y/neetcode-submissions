class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        h={}
        for i in n:
            if(i in h.keys()):
                return i
            else:
                h[i]=0

        
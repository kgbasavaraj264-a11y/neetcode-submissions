class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        x=sorted(a)
        y=sorted(b)
        if x==y:
            return True
        else:
            return False
        
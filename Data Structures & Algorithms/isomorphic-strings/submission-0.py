class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        h={}
        for i in range(len(a)-1+1):
            if a[i] in h.keys() and h[a[i]]!=b[i]:
                return False
            elif a[i] not in h.keys() and b[i] in h.values():
                return False
            else:
                h[a[i]]=b[i]
        return True
        
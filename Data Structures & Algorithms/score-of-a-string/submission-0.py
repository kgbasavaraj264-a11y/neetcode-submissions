class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in s:
            l.append(ord(i))
        a=0
        for i in range(len(l)-1):
            sum=abs(l[i+1]-l[i])
            a=a+sum
        return a
        
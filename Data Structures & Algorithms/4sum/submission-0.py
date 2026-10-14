class Solution:
    def fourSum(self, n: List[int], target: int) -> List[List[int]]:
        n.sort()
        a=[]
        i=0
        while(i<len(n)-1):
            j=i+1
            while(j<len(n)-1):
                k=j+1
                l=len(n)-1
                while(k<l):
                    if(n[i]+n[j]+n[k]+n[l]==target):
                        t=[]
                        t.append(n[i])
                        t.append(n[j])
                        t.append(n[k])
                        t.append(n[l])   
                        if t not in a:
                            a.append(t)   
                        k=k+1
                        l=l-1
                    elif(n[i]+n[j]+n[k]+n[l]>target):
                        l=l-1
                    else:
                        k=k+1
                j=j+1
            i=i+1
        return a


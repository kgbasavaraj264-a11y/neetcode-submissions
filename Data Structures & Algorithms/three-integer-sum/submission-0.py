class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        ans=[]
        i=0
        while(i<len(n)):
            j=i+1
            k=len(n)-1
            while(j<k):
                if(n[i]+n[j]+n[k]==0):
                    t=[]
                    t.append(n[i])
                    t.append(n[j])
                    t.append(n[k])
                    if t not in ans:
                        ans.append(t)
                    j=j+1
                    k=k-1
                elif(n[i]+n[j]+n[k]>0):
                    k=k-1
                else:
                    j=j+1
            i=i+1
        return ans

        
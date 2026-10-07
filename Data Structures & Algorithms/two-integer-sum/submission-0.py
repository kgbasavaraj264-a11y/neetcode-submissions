class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        h={}
        i=0
        for x in nums:
            if target-x in h.keys():
                ans.append(h[target-x])
                ans.append(i)
            else:
                h[x]=i
            i=i+1
        return ans

        
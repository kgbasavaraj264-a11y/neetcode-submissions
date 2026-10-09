class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h={}
        sum=0
        submax=nums[0]
        for i in nums:
            sum=max(sum+i,i)
            submax=max(submax,sum)
        return submax
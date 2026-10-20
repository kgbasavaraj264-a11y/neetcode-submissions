class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=[0]*len(prices)
        q=0
        m[0]=prices[0]
        for i in range(1,len(prices)):
            m[i]=min(prices[i],m[i-1])
        for i in range(1,len(prices)):
            q=max(q,prices[i]-m[i-1])
        return q
        
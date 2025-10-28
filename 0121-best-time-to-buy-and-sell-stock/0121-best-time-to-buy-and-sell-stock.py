class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float('inf')
        profit=0

        for i in range(len(prices)):
            m=min(m,prices[i])
            profit=max(profit,prices[i]-m)
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        p=0
        cp=prices[0]

        for i in range(len(prices)):
            cp=min(cp,prices[i])
            for j in range(i+1,len(prices)):
                p=max(p,prices[j]-cp)
        return p
        """
        cp=prices[0]
        p=0

        for num in prices:
            cp=min(cp,num)
            p=max(p,num-cp)
        return p
        
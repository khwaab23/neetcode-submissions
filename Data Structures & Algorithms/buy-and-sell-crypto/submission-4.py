class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        l=0
        for r in range(1,len(prices)):
            if prices[l]>=prices[r]:
                l=r
                continue
            maxProfit=max(maxProfit,prices[r]-prices[l])
        return maxProfit
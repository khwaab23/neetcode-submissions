class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        dp=[[0]*2 for _ in range(len(prices)+2)]

        for i in range(len(prices)-1, -1, -1):
            for buying in [True,False]:

                cooldown=dp[i+1][buying]

                if buying:
                    buy=dp[i+1][False]-prices[i]
                    dp[i][1]=max(buy,cooldown)
                
                else:
                    sell=dp[i+2][1]+prices[i]
                    dp[i][0]=max(sell,cooldown)
                
        return dp[0][1]
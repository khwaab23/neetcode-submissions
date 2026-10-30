class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        coins.sort()
        for i in range(1,amount+1):
            minimum=float('inf')
            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                minimum=min(minimum,dp[diff]+1)
            dp[i]=minimum

        if dp[amount]<float('inf'):
            return dp[amount]
        
        else:
            return -1
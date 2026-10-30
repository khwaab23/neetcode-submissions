class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(1,amount+1):
                diff=i-coin
                if diff<0:
                    continue
                dp[i]=min(dp[diff]+1,dp[i])
            
        return dp[-1] if dp[-1]!=float('inf') else -1
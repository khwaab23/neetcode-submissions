class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(weight)
        dp=[[0]*(capacity+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,capacity+1):
                if weight[i-1]<=j:
                    dp[i][j]=max(profit[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]


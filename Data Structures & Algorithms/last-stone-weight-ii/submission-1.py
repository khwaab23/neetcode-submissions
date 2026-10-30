class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum=sum(stones)
        target=stoneSum//2

        dp=[[0]*(target+1) for _ in range(len(stones)+1)]
        
        # for i in range(1,len(stones)+1):
        #     dp[i][0]=stones[i-1]
        for i in range(1,len(stones)+1):
            for j in range(1,target+1):
                if stones[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-stones[i-1]]+stones[i-1])
                else:
                    dp[i][j]=dp[i-1][j]
        
        return stoneSum-2*dp[-1][-1]


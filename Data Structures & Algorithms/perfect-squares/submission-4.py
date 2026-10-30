class Solution:
    def numSquares(self, n: int) -> int:
        
        res=[]
        for i in range(1,n+1):
            if i**2<=n:
                res.append(i**2)
            else:break
        
        # [1,4,9],amount=13
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for r in res:
                diff=i-r
                if diff<0:
                    continue
                dp[i]=min(dp[i],dp[diff]+1)
        print(res)
        print(dp)
        return dp[-1]

        
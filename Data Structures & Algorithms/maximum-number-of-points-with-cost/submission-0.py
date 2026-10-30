class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows=len(points)
        cols=len(points[0])
        
        dp=[[0]*(cols) for _ in range(rows)]

        for i in range(cols):
            dp[0][i]=points[0][i]

        for i in range(1,rows):
            for j in range(cols):
                for c in range(cols):
                    dp[i][j]=max(dp[i][j],points[i][j]+dp[i-1][c]-abs(c-j))
        print(dp)
        return max(dp[-1])
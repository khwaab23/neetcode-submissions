class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True

        for i in range(n-1,-1,-1):
            for word in wordDict:
                j=len(word)
                if i+j<=len(s) and s[i:i+j]==word:
                    dp[i]=dp[i+j]
                if dp[i]:
                    break
        return dp[0]
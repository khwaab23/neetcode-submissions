class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxlen=0
        res=[-1,-1]
        for i in range(n):
            l,r=i,i
            while l>=0 and r<n and s[r]==s[l]:
                if r-l+1>maxlen:
                    maxlen=r-l+1
                    res=[l,r]
                r+=1
                l-=1
            
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>maxlen:
                    maxlen=r-l+1
                    res=[l,r]
                r+=1
                l-=1
        l,r=res
        return s[l:r+1]
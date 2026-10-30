class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resLen,resIdx=0,[-1,-1]

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[r]==s[l]:
                
                if resLen<=r-l+1:
                    resLen=r-l+1
                    resIdx=[l,r]
                l-=1
                r+=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                 
                if resLen<r-l+1:
                    resLen=r-l+1
                    resIdx=[l,r]

                l-=1
                r+=1
        l,r=resIdx
        return s[l:r+1]

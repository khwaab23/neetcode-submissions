class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        l=0
        maxlen=0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l+=1
            
            check.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen
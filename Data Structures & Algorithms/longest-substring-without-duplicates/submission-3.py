class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        hashset=set()
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            
            hashset.add(s[r])
            maxlen=max(maxlen,r-l+1)

        return maxlen

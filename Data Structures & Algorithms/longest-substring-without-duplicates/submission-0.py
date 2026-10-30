class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        set1=set()
        maxlen=0
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[l])
                l+=1
        
            set1.add(s[r])
        

            maxlen=max(maxlen,r-l+1)

            
        return maxlen


            
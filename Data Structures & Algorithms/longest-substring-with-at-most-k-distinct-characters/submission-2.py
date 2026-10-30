class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return k
        window=defaultdict(int)
        l=0
        maxLen=0

        for r in range(len(s)):
            window[s[r]]+=1
            while len(window)>k:
                window[s[l]]-=1
                if window[s[l]]==0:
                    del window[s[l]]
                l+=1
            
            maxLen=max(maxLen,r-l+1)
        return maxLen
                
                


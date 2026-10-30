class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        max_string=0
        l=0
        window_hash=Counter()
      
        for r in range(len(s)):
            window_hash[s[r]]+=1
    
            while len(window_hash)>2:
                window_hash[s[l]]-=1
                if window_hash[s[l]] == 0:
                    del window_hash[s[l]]
                l+=1
                
                
            max_string=max(max_string,r-l+1)
            

        return max_string
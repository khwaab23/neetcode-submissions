class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        window=defaultdict(int)
        l=0
        res=0
        for r in range(len(s)):
            window[s[r]]+=1
            while window[s[r]] > 1 or (r - l + 1) > k:
                window[s[l]]-=1
                if window[s[l]]==0:
                    del window[s[l]]
                l+=1
            if r-l+1==k:
                res+=1
        return res
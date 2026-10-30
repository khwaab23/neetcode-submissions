class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        windowS={}
        windowT={}

        have=need=0
        minlen=float('inf')
        for i in t:
            windowT[i]=1+windowT.get(i,0)
        need=len(windowT)
        l=0    
        res=""    
        for r in range(len(s)):
            windowS[s[r]]=1+windowS.get(s[r],0)
            if s[r] in windowT and windowS[s[r]]==windowT[s[r]]:
                have+=1
            
            while have==need:
                if r-l+1<minlen:
                    res=s[l:r+1]
                    minlen=r-l+1
                windowS[s[l]]-=1
                if s[l] in windowT and windowS[s[l]] < windowT[s[l]]:
                    have-=1
                l+=1
        return res

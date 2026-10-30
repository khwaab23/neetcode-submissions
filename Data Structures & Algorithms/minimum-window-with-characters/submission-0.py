class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        l=0
        res,resLen=[-1,-1],float('inf')
        countT,windowT={},{}
        for i in t:
            countT[i]=1+countT.get(i,0)

        have=0
        need=len(countT)

        for r in range(len(s)):
            windowT[s[r]]=1+windowT.get(s[r],0)
            if s[r] in countT and countT[s[r]]==windowT[s[r]]:
                have+=1
            
            while have==need:
                windowT[s[l]]-=1

                if r-l+1<resLen:
                    res=[l,r]
                    resLen=r-l+1

                if s[l] in countT and windowT[s[l]]<countT[s[l]]:
                    have-=1
                l+=1

        l,r=res
        return s[l:r+1] if resLen != float('inf') else ""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen=0
        maxfreq=0
        counter={}
        i=0
        for j in range(len(s)):
            counter[s[j]]=1+counter.get(s[j],0)
            maxfreq=max(maxfreq,counter[s[j]])
            while j-i+1>maxfreq+k:
                counter[s[i]]-=1
                i+=1
            
            maxlen=max(maxlen,j-i+1)
        
        return maxlen
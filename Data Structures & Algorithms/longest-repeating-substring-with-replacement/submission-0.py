class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        res=0
        maxf=0
        count={}

        for j in range(len(s)):
            count[s[j]]=1+count.get(s[j],0)
            maxf=max(maxf,count[s[j]])
            

            while (j-i+1)>k+maxf:
                count[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res


            

        
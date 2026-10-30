class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        subres=[]
        n=len(s)
        def backtrack(i):
            if i==n:
                copy=" ".join(subres)
                res.append(copy)
                return
            
            for j in range(i,n):
                w=s[i:j+1]
                if w in wordDict:
                    subres.append(w)
                    backtrack(j+1)
                    subres.pop()



        backtrack(0)
        return res
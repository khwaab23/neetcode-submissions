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
                for w in wordDict:
                    if s[i:j+1]==w:
                        subres.append(s[i:j+1])
                
                        backtrack(j+1)

                        subres.pop()
        



        backtrack(0)
        return res
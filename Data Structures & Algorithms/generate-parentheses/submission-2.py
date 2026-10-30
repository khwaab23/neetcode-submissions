class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        subres=[]
        if n==0:
            return []
        def backtrack(openN,closeN):
            if openN==closeN and openN==n:
                copy="".join(subres)
                res.append(copy)
                return
            
            if closeN>openN or openN>n:
                return
            
            if openN<n:
                subres.append("(")
                backtrack(openN+1,closeN)
                subres.pop()
            if closeN<openN:
                subres.append(")")
                backtrack(openN,closeN+1)
                subres.pop()
            
        
        backtrack(0,0)
        return res
            
            
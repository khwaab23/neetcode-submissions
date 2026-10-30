class Solution:
    def totalNQueens(self, n: int) -> int:
        res=0

        posDiag=set()
        negDiag=set()
        col=set()

        def backtrack(r):
            nonlocal res

            if r==n:
                res+=1
            
            
            for c in range(n):
                if r-c in negDiag or r+c in posDiag or c in col:
                    continue
                
                posDiag.add(r+c)
                negDiag.add(r-c)
                col.add(c)

                backtrack(r+1)

                posDiag.remove(r+c)
                negDiag.remove(r-c)
                col.remove(c)

        backtrack(0)
        return res
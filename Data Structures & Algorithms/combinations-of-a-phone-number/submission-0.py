class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        comb={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        subres=[]
        def backtrack(i):
            if len(subres)==len(digits):
                copy="".join(subres.copy())
                res.append(copy)
                return
            
            if i>len(digits):
                return

            for d in comb[digits[i]]:
                subres.append(d)
                backtrack(i+1)
                subres.pop()

        backtrack(0)
        return res
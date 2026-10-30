class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        subset=[]
        digit={
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def dfs(i):
            if len(subset)==len(digits):
                copy="".join(subset)
                res.append(copy)
                return
            
            if i>=len(digits):
                return

            for d in digit[digits[i]]:
                subset.append(d)
                dfs(i+1)
                subset.pop()
            
        dfs(0)
        return res



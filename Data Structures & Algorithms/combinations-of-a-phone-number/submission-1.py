class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        subset=[]
        digit={
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }

        def combination(i):
            if i==len(digits) and len(subset)==len(digits):
                ans="".join(subset)
                res.append(ans)
                return
            if i >=len(digits):
                return
            
            for j in digit[digits[i]]:
                subset.append(j)
                combination(i+1)
                subset.pop()
                combination(i+1)
        

        combination(0)
        return res
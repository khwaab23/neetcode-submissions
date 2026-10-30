class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset=[]
        res=[]
        candidates.sort()
        def backtrack(i):
            
            if sum(subset)==target and subset not in res:
                res.append(subset.copy())
                return
            
            if sum(subset)>target or i>=len(candidates):
                return
            
            subset.append(candidates[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res
            
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset=[]
        res=[]
        def dfs(i):
            if sum(res)==target and res not in subset:
                subset.append(res.copy())
            if sum(res)>target or i>=len(candidates):
                return 

            res.append(candidates[i])
            dfs(i+1)
            res.pop()
            dfs(i+1)
        dfs(0)
        return subset
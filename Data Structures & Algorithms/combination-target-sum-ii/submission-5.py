class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset=[]
        curset=[]
        candidates.sort()
        def dfs(i,candidates,curset,subset):
            
            if sum(curset)==target and curset not in subset:
                
                subset.append(curset.copy())
                return 

            if i>=len(candidates) or sum(curset)>target:
                return


            curset.append(candidates[i])
            dfs(i+1,candidates,curset,subset)
            curset.pop()
            dfs(i+1,candidates,curset,subset)

        dfs(0,candidates,curset,subset)
        return subset
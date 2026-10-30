class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset=[]
        res=[]
        candidates.sort()
        def backtrack(i):
            if sum(subset)==target and subset not in res:
                res.append(subset[:]) #res.append(subset[:])
            
            if i>=len(candidates) or sum(subset)>target:
                return 
            
            subset.append(candidates[i])

            backtrack(i+1)
            subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1)
            
        

        backtrack(0)
        return res
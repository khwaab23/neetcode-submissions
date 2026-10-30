class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if sum(res)==target:
                subset.append(res.copy())
                
                return 
            
            if sum(res)>target:
                
                return

            if i>=len(nums):
                return 

            res.append(nums[i])
            dfs(i)
            res.pop()
            dfs(i+1)
        
        dfs(0)

        return subset
            

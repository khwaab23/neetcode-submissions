class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset=[]
        curset=[]
        def dfs(i):
            if target==sum(curset):
                subset.append(curset.copy())
                return 
            if sum(curset)>target or i>=len(nums):
                return 
            
            curset.append(nums[i])
            dfs(i)
            curset.pop()
            dfs(i+1)
        dfs(0)
        return subset
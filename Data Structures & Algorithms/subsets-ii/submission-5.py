class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def dfs(i):
            if i==len(nums) and subset not in res:
                res.append(subset.copy())
                return
            if subset in res or i>=len(nums):
                return
            

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def dfs(i):
            # res.sort()
            if res in subset:
                return
            if i>=len(nums):
                subset.append(res.copy())
                return

            res.append(nums[i])
            dfs(i+1)
            res.pop()
            dfs(i+1)
        dfs(0)
        return subset

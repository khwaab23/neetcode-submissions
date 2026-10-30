class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        curset=[]
        nums.sort()
        def dfs(i,nums,curset,subset):
            if i>=len(nums) and curset not in subset:
                subset.append(curset.copy())
                return 
            if curset in subset:
                return 
            curset.append(nums[i])
            dfs(i+1,nums,curset,subset)
            curset.pop()
            # while i+1<len(nums) and nums[i]==nums[i+1]:
            #     i+=1
            dfs(i+1,nums,curset,subset)

        dfs(0,nums,curset,subset)
        return subset
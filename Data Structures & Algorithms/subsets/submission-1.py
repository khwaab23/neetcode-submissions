class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset,curset=[],[]
        def helper(i,nums,subset,curset):
            if i >=len(nums):
                subset.append(curset.copy())
                return
            curset.append(nums[i])
            helper(i+1,nums,subset,curset)
            curset.pop()
            helper(i+1,nums,subset,curset)
        helper(0,nums,subset,curset)
        return subset
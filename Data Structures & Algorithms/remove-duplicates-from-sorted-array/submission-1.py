class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for x in range(len(nums)-1,0,-1):
            if(nums[x]==nums[x-1]):
                nums.pop(x)
        return len(nums)
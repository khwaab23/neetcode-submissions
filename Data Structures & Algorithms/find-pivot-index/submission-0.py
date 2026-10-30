class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1=sum(nums)
        
        prefix=0
        for i in range(len(nums)):
            if 2*prefix==s1-nums[i]:
                return i
            prefix+=nums[i]
        return -1

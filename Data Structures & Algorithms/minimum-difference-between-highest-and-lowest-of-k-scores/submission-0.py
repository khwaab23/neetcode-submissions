class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        minval=float('inf')
        for r in range(k-1,len(nums)):
            minval=min(minval,nums[r]-nums[l])
            l+=1
        return minval
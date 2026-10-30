class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currSum=0
        for n in nums:
            currSum+=n
            maxsum=max(maxsum,currSum)
            currSum=max(currSum,0)
            

        return maxsum
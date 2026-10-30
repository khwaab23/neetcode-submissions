class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum1=0
        maxsum=0
        lastnum=0
        for num in nums:
            if num<=lastnum:
                sum1=0
            sum1+=num
            maxsum=max(maxsum,sum1)
            lastnum=num
        return maxsum
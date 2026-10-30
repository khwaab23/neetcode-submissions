class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minimum=1
        maximum=1
        maxval=nums[0]
        for num in nums:
            temp=maximum*num
            maximum=max(temp,minimum*num,num)
            minimum=min(temp,minimum*num,num)
            maxval=max(maxval,maximum)
        return maxval
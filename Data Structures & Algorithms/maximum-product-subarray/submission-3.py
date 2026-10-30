class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=1
        minimum=1
        maxval=nums[0]
        for num in nums:
            temp=maximum*num
            maximum=max(temp,num*minimum,num)
            minimum=min(temp,num*minimum,num)
            maxval=max(maxval,maximum)
        return maxval
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=minimum=1
        maxProd=nums[0]
        for num in nums:
            temp=num*maximum
            maximum=max(temp,minimum*num,num)
            minimum=min(temp,minimum*num,num)
            maxProd=max(maxProd,maximum)
        return maxProd
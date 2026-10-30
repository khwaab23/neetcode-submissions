class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #We will use kadane's algorithm
        maxprod=nums[0]
        minimum=maximum=1
        for num in nums:
            temp=maximum*num
            maximum=max(maximum*num,minimum*num,num)
            minimum=min(temp,minimum*num,num)
            maxprod=max(maximum,maxprod,)
        return maxprod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp=minp=1
        res=nums[0]
        for num in nums:
            temp=maxp*num
            maxp=max(maxp*num,minp*num,num)
            minp=min(temp,minp*num,num)
            res=max(res,maxp)
        return res
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=1,1
        arr=[1]*len(nums)

        for i in range(len(nums)):
            arr[i]*=l
            l*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            arr[i]*=r
            r*=nums[i] 
        return arr

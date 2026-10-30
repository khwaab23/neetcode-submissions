class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res=len(nums)
        l,r=0,len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res
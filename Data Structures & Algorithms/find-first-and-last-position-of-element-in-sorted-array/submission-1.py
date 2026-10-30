class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l,r=0,len(nums)-1
        while l<=r:
            print("hi")
            mid=(l+r)//2
            print(mid)
            if nums[mid]==target:
                print("hello")
                break
            
            elif nums[mid]>target:
                print("first")
                r=mid-1
            elif nums[mid]<target:
                print("second")
                l=mid+1
        
        if nums[mid]!=target:
            return[-1,-1]
        
        l,r=mid,mid
        while l>=0 and nums[l]==target:
            l-=1
        
        while r<len(nums) and nums[r]==target:
            r+=1
        
        return [l+1,r-1]
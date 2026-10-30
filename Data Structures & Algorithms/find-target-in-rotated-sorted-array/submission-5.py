class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid

            if nums[l]<=nums[mid]:
                # we are in the left sorted array
                if target>nums[mid] or target<nums[l]:
                        l=mid+1
                else:
                        r=mid-1

            else:
                # we are in the right sorted array
                # [5,6,1,2,3,4]
                # [6,1,2,3,4,5]
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1

        return -1
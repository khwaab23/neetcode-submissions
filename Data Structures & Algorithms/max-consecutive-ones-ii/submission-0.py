class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        can_flip=True
        l=0
        max1=0
        for r in range(len(nums)):

            if not can_flip and nums[r]==0:
                while nums[l]!=0:
                    l+=1
                can_flip=True
                l+=1

            if nums[r]==0  :
                can_flip=False
            max1=max(max1,r-l+1)
        return max1
            
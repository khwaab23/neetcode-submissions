class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res=0
        nums.sort()
        r=len(nums)-1
        mod=10**9+7
        for i,l in enumerate(nums):
            while i<=r and l+nums[r]>target:
                r-=1
            
            if i<=r:
                res+=pow(2,r-i,mod)
                res%=mod
        return res
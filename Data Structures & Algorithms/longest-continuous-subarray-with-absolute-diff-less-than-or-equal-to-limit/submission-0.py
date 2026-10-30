class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res=0
        for i in range(len(nums)):
            minimum=maximum=nums[i]
            for j in range(i, len(nums)):
                minimum=min(nums[j],minimum)
                maximum=max(nums[j],maximum)
                if maximum-minimum>limit:
                    break
                res=max(res,j-i+1)
        return res
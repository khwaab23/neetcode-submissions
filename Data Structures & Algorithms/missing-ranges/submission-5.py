class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res=[]
        if not nums:
            return [[lower,upper]]
        if lower<nums[0]:
            res.append([lower,nums[0]-1])
        for j in range(len(nums)-1):
            if nums[j+1]-nums[j]<=1:
                continue
            

            res.append([nums[j]+1,nums[j+1]-1])
        
        if upper>nums[-1]:
            res.append([nums[-1]+1,upper])
        return res
            

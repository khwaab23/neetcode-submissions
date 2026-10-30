class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxlength=0
        for num in nums:
            length=0
            while num-1 in numset:
                num-=1
            
            while num+length in numset:
                length+=1
            maxlength=max(maxlength,length)
        return maxlength
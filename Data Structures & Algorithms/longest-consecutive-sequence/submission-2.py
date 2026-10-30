class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        i=0
        maxLen=0
        for num in numset:
            if num-1 in numset:
                continue
            length=0
            while num+length in numset:
                length+=1
            maxLen=max(maxLen,length)

        return maxLen
            
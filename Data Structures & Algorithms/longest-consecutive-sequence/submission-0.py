class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        maxl=0
        for num in numset:
            if num-1 not in numset:
                longest=1
                while num+longest in numset:
                    longest+=1

            maxl=max(maxl,longest)

        return maxl
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxlen=0
        for num in nums:
            if num-1 in nums:
                continue

            length=0
            while num+length in nums:
                length+=1

            maxlen=max(maxlen,length)
        return maxlen 

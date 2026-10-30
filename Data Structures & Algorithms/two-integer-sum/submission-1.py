class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1={}
        for key,val in enumerate(nums):
            if target-val in hash1:
                return[hash1[target-val],key]
            hash1[val]=key
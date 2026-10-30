class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        # for k ,v in count.items():
        nums.sort(key= lambda n:(count[n],-n))
        return nums

            

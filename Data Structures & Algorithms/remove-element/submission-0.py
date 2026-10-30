class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for x in range (len(nums)-1,-1,-1):
            if(nums[x]== val):
                nums.pop(x)
                continue;
        return len(nums)
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nums[:]=nums[n-k%n:]+nums[:n-k%n]
        print(nums)


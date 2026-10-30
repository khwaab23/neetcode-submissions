class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        # start=n-2
        goal=n-1
        for start in range(n-2,-1,-1):
            if nums[start]+start>=goal:
                goal=start
               
        print(goal)
        return goal==0
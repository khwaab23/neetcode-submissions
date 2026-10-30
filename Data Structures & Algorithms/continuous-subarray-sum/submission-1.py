class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total=0
        remainder={0:-1}

        for i,n in enumerate(nums):
            total+=n
            r=total%k
            if r not in remainder:
                remainder[r]=i
            elif i-remainder[r]>1:
                return True
        return False
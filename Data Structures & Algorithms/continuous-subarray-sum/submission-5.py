class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={0:-1}

        total=0
        for i,num in enumerate(nums):
            total+=num
            r=total%k
            if r in remainder:
                if (i-remainder[r]>=2):
                    return True
            else:
                remainder[r]=i
        return False
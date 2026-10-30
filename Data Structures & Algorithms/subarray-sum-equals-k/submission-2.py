class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total=count=0
        hash1={0:1}

        for n in nums:
            total+=n    
            if total-k in hash1:
                count+=hash1[total-k]
            hash1[total]=1+hash1.get(total,0)

        return count
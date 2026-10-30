class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash1={0:1}
        total=0
        cnt=0
        for num in nums:
            total+=num
            if total-k in hash1:
                cnt+=hash1[total-k]
            hash1[total]=1+hash1.get(total,0)

        return cnt
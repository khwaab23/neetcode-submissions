class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for x in range(2):
            for num in nums:
               ans.append(num)
        return ans
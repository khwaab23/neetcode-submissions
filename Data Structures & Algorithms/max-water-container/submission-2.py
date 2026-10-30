class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxWater=0
        while i<j:
            if heights[i]<=heights[j]:
                maxWater=max(maxWater,heights[i]*(j-i))
                i+=1
            else:
                maxWater=max(maxWater,heights[j]*(j-i))
                j-=1
        return maxWater
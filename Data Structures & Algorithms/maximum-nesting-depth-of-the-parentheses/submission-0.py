class Solution:
    def maxDepth(self, s: str) -> int:
        res=max1=0
        for i in s:
            if i=="(":
                res+=1
            elif i==")":
                res-=1
            max1=max(max1,res)
        return max1
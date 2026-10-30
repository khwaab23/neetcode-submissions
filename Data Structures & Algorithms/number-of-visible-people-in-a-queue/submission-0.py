class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res=[0]*len(heights)
        stack=[]
        for i,h in enumerate(heights):

            while stack and stack[-1][1]<=h:
                idx,ht=stack.pop()
                res[idx]+=1
            
            if stack:
                res[stack[-1][0]]+=1
            
            stack.append((i,h))

        


        return res
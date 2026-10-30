class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        
        directions=[[0,1],[1,0],[-1,0],[0,-1]]

        rows=len(image)
        cols=len(image[0])
        q=deque([(sr,sc,image[sr][sc])])
        image[sr][sc]=color
        visit=set()

        while q:
            for _ in range(len(q)):
                r,c,prevVal=q.popleft()
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if min(row,col)<0 or row==rows or col==cols or image[row][col]!=prevVal or (row,col) in visit:
                        continue
                    
                    q.append((row,col,image[row][col]))
                    visit.add((row,col))
                    image[row][col]=color
            
        return image
                    
                    
                    

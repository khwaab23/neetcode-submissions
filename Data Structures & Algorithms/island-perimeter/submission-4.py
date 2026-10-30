class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visit=set()
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    q.append((r,c))
                    visit.add((r,c))
                    break
            
        
        
        perimeter=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    

                    if min(row,col)<0 or row==rows or col==cols or grid[row][col]==0:
                        perimeter+=1
                        continue
                    if (row,col) not in visit:
                        visit.add((row,col))
                        q.append((row,col))
        return perimeter


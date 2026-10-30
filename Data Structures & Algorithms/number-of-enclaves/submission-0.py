class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        


        
        for r in range(rows):
            for c in [0,cols-1]:
                if grid[r][c]==1:
                    q.append((r,c))
        for r in [0,rows-1]:
            for c in range(cols):
                if grid[r][c]==1:
                    q.append((r,c))
        
        visit=set()

        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                visit.add((r,c))
                grid[r][c]=0
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if min(row,col)<0 or row==rows or col==cols or grid[row][col]==0 or (row,col) in visit:
                        continue
                    
                    q.append((row,col))
                    visit.add((row,col))
                    grid[row][col]=0
        enclaves=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    enclaves+=1
        
        return enclaves


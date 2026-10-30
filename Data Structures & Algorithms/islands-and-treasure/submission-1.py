class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        visit=set()
        inf=2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            r,c=q.popleft()
            distance=0
            for dr,dc in directions:
                row,col=dr+r,dc+c
                while 0<=row<rows and 0<=col<cols and grid[row][col]==inf and (row,col) not in visit:
                    distance+=1
                    grid[row][col]=grid[r][c]+1
                    q.append((row,col))
                    visit.add((row,col))
                    
        return 

            

        

        




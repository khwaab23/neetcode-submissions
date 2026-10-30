class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        visited=set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))
        inf=2147483647
        def addCell(r,c):
            if 0<=r<rows and 0<=c<cols and grid[r][c]==inf and (r,c) not in visited:
                q.append((r,c))
                visited.add((r,c))


        distance=0
        while q:
            
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=distance
                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r,c-1)
                addCell(r-1,c)
            distance+=1
        
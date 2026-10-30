class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        found=False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c]==1:
                    q.append((r,c))
                    grid[r][c]=2
                    found=True
                    break
        q2=deque()
        while q:
            r,c=q.popleft()
            q2.append((r,c))
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]!=1:
                    continue
                
                q.append((row,col))
                grid[row][col]=2
        res=0   
        while q2:
            for _ in range(len(q2)):
                r,c=q2.popleft()
                
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]==2:
                        continue
                    
                    if grid[row][col]==1:
                        return res
                    elif grid[row][col]==0:
                        q2.append((row,col))     
                        grid[row][col]=2
            res+=1

        return res           
                
                
        

        

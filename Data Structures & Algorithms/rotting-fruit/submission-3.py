class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        fresh_cnt=0
        q=deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_cnt+=1
                if grid[r][c]==2:
                    q.append((r,c))
                


        minutes=0
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        while fresh_cnt>0 and q:
            
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr , dc in directions:
                    row=r+dr
                    col=c+dc
                
                    if 0<=row<rows and 0<=col<cols and grid[row][col]==1 :
                        grid[row][col]=2
                        
                        q.append((row,col))
                        fresh_cnt-=1
            minutes+=1

        # def addCell(r,c):
        #     nonlocal fresh_cnt
        #     if 0<=r<rows and 0<=c<cols and grid[r][c]==1 and (r,c) not in visited :
        #         grid[r][c]=2
        #         fresh_cnt-=1
        #         q.append((r,c))
        #         visited.add((r,c))
                
            
        # minutes=0
        # while q:
        #     minutes+=1
        #     for _ in range(len(q)):
        #         r,c=q.popleft()
        #         addCell(r+1,c)
        #         addCell(r-1,c)
        #         addCell(r,c+1)
        #         addCell(r,c-1)
            

        return minutes if fresh_cnt==0 else -1
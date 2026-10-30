class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        q=deque()
        visit=set()
        rows=len(grid)
        cols=len(grid[0])

        fresh_cnt=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c]==1:
                    fresh_cnt+=1
        
        minutes=0
        while q and fresh_cnt>0:
            minutes+=1
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or grid[row][col]==0:
                        continue
                    fresh_cnt-=1
                    visit.add((row,col))
                    q.append((row,col))


           
        
        return minutes if fresh_cnt==0 else -1


        

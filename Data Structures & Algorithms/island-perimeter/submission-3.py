class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q=deque()
        visit=set()
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(grid)
        cols=len(grid[0])
        found=False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    q.append((i,j))
                    visit.add((i,j))
                    found=True
                    break
            if found: break
        per=0
        while q:
            row,col=q.popleft()
            for dr,dc in directions:
                r=row+dr
                c=col+dc
                if r<0 or r>=rows or c<0 or c>=cols or (grid[r][c]==0):
                    per+=1
                    continue
                if (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
        return per

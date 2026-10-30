class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        visit=set()

        def bfs(r,c):
            Area=1
            q.append((r,c))
            visit.add((r,c))
            while q:
                r1,c1=q.popleft()
                for dr,dc in directions:
                    row=dr+r1
                    col=dc+c1
                    if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or grid[row][col]==0:
                        continue
                    
                    q.append((row,col))
                    visit.add((row,col))
                    Area+=1
            return Area
        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area=bfs(r,c)
                    maxArea=max(maxArea,area)
        
        return maxArea
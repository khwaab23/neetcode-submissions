class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        q=deque()
        visit=set()
        directions=[[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(r,c):
            visit.add((r,c))
            q.append((r,c))
            Area=1

            while q:
                for _ in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        row,col=dr+r,dc+c
                        if min(row,col)<0 or row==rows or col==cols or grid[row][col]==0 or (row,col) in visit:
                            continue
                        
                        Area+=1
                        q.append((row,col))
                        visit.add((row,col))
            return Area

            

        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxArea=max(maxArea,bfs(r,c))

        return maxArea


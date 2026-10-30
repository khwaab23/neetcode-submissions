class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def bfs(r,c):
            grid[r][c]='.'
            q=deque()
            q.append((r,c))
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            maxArea=1
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if 0<=row<rows and 0<=col<cols and grid[row][col]==1:
                        grid[row][col]='.'
                        q.append((row,col))
                        maxArea+=1
            # return maxArea
                    
            return maxArea


        maxArea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea=max(maxArea,bfs(r,c))

        return maxArea
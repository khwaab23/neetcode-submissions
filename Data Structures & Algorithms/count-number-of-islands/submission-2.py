class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        
        def bfs(r,c):
            q.append((r,c))
            while q:

                for _ in range(len(q)):
                    r,c=q.popleft()
                    for dr,dc in directions:
                        row,col=r+dr,c+dc
                        if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]=="0" or (row,col) in visit:
                            continue
                        q.append((row,col))
                        visit.add((row,col))

                
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands



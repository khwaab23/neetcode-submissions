class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        visit=set()
        
        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                r1,c1=q.popleft()
                for dr, dc in directions:
                    row=r1+dr
                    col=c1+dc
                    if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]=="0" or (row,col) in visit:
                        continue
                    
                    q.append((row,col))
                    visit.add((row,col))
                


        
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)

        return islands
        

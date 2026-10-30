class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        visit=set()

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                for _ in range(len(q)):
                    curr_r,curr_c=q.popleft()
                    for dr,dc in directions:
                        row=curr_r+dr
                        col=curr_c+dc
                        if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or grid[row][col]=="0":
                            continue
                        q.append((row,col))
                        visit.add((row,col))


        islands=0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1

        return islands

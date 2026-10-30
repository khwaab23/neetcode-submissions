class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        connected_island=set()
        q=deque()
        unique_islands=set()
        visit=set()
        def bfs(r,c):
            connected_island=set()
            origin_r=r
            origin_c=c
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or not grid[row][col]:
                        continue
                    
                    q.append((row,col))
                    visit.add((row,col))
                    connected_island.add((row-origin_r,col-origin_c))
            return frozenset(connected_island)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in visit:
                    unique_islands.add(bfs(r,c))
        
        return len(unique_islands)
                



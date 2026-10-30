class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        minLen=float('inf')
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visit=set()
        q=deque()
        q.append((0,0,0))
        while q:
            for _ in range(len(q)):
                r,c,countstep=q.popleft()
                visit.add((r,c))
                if r==rows-1 and c==cols-1:
                    minLen=min(countstep,minLen)

                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if min(row,col)<0 or row==rows or col==cols or grid[row][col]==1 or (row,col) in visit:
                        continue
                    
                    
                    q.append((row,col,countstep+1))

        return minLen if minLen!=float('inf') else -1

                    

        
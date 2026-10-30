class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        minLen=float('inf')
        rows,cols=len(grid),len(grid[0])
        q=deque()
        q.append((0,0,0))
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visit=set()
        visit.add((0,0))
        while q:
            for _ in range(len(q)):
                r,c,pathlen=q.popleft()
                if r==rows-1 and c==cols-1:
                        minLen=min(minLen,pathlen)
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if min(row,col)<0 or row>=rows or col>=cols or grid[row][col]==1 or (row,col) in visit:
                        continue
                    
                    visit.add((row,col))
                    q.append((row,col,pathlen+1))

        


        return minLen if minLen!=float('inf') else -1
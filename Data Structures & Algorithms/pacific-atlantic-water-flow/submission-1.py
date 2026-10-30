class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions=[[0,1],[-1,0],[0,-1],[1,0]]
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()
        q=deque()
        

        def bfs(r,c,visit,prevH):
            q.append((r,c))
            visit.add((r,c))
            while q:
                r1,c1=q.popleft()
                for dr,dc in directions:
                    row=dr+r1
                    col=dc+c1
                    if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or heights[r1][c1]>heights[row][col]:
                        continue
                    
                    visit.add((row,col))
                    q.append((row,col))
        

        for r in range(rows):
        
            bfs(r,0,pac,heights[r][0])
            bfs(r,cols-1,atl,heights[r][cols-1])
        
        for c in range(cols):
            bfs(0,c,pac,heights[0][c])
            bfs(rows-1,c,atl,heights[rows-1][c])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res





        


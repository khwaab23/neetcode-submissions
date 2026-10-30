class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])

        pacific=[[False]*cols for _ in range(rows)]
        atlantic=[[False]*cols for _ in range(rows)]

        pac=set()
        atl=set()

        def dfs(r,c,visited,prevHeight):
            if 0<=r<rows and 0<=c<cols and (r,c) not in visited and prevHeight<=heights[r][c] :
                visited.add((r,c))
                dfs(r+1,c,visited,heights[r][c])
                dfs(r-1,c,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])


        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
            
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res


        
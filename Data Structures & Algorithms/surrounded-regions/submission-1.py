class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        directions=[[0,1],[-1,0],[0,-1],[1,0]]
        q=deque()
        visit=set()

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                r1,c1=q.popleft()
                for dr,dc in directions:
                    row=r1+dr
                    col=dc+c1
                    if min(row,col)<0 or row>=rows or col>=cols or (row,col) in visit or board[row][col]=='X':
                        continue
                    q.append((row,col))
                    visit.add((row,col))
                    board[row][col]='T'

        for r in range(rows):
            for c in [0,cols-1]:
                if board[r][c]=='O':
                    board[r][c]='T'
                    bfs(r,c)
        
        for r in [0,rows-1]:
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='T'
                    bfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='T':
                    board[r][c]='O'
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c):
            if 0<=r<rows and 0<=c<cols and board[r][c]=='O':
                board[r][c]='T'
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'
        

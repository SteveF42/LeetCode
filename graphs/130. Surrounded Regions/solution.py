class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # O(n*m) time 
        # O(n*m) space
        """
        Do not return anything, modify board in-place instead.
        """
        ROW,COL = len(board),len(board[0])
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or (r,c) in visited or board[r][c] == 'X':
                return
            visited.add((r,c))
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(COL):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[ROW-1][i] == 'O':
                dfs(ROW-1,i)
            
        for i in range(ROW):
            board[i][0]
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][COL-1] == 'O':
                dfs(i,COL-1)
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'T':
                    board[i][j] = 'O'
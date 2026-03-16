import sys

def solve():
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

    r, c = map(int, sys.stdin.readline().split())

    min_moves = float('inf')
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(cr, cc, apples, moves):
        nonlocal min_moves
        
        if apples == 3:
            min_moves = min(min_moves, moves)
            return
        
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] != -1:
                
                temp = board[nr][nc]
                
                board[nr][nc] = -1
                
                next_apples = apples + 1 if temp == 1 else apples
                dfs(nr, nc, next_apples, moves + 1)
                
                board[nr][nc] = temp

    start_apples = 1 if board[r][c] == 1 else 0
    temp_start = board[r][c]
    board[r][c] = -1 
    
    dfs(r, c, start_apples, 0)
    
    if min_moves == float('inf'):
        print(-1)
    else:
        print(min_moves)

solve()
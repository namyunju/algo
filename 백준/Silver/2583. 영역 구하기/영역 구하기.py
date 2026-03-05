import sys
input = sys.stdin.readline
from collections import deque

M,N,K = map(int, input().split())
# M행 N열
board = [[0]*N for _ in range(M)]
# 0 2 4 4 입력되면
# 0과 4는 열을, 2와 4는 행을
# 0열부터 3열까지
# 아래에서부터 2,3 . 위에서부터 세면 1,2 즉 M-1-3부터 M-1-2

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(M-r2, M-r1):
        for c in range(c1,c2):
            board[r][c] = 1

ans = []
def solve(i,j):
    q = deque([(i,j)])
    region = 1
    
    while q:
        x,y = q.popleft()
        board[x][y] = 1
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = x+dx, y+dy
            if 0<= nx < M and 0 <= ny < N:
                if board[nx][ny] == 0:
                    q.append([nx,ny])
                    board[nx][ny] = 1
                    region += 1
    ans.append(region)

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            solve(i,j)

ans.sort()
print(len(ans))
print(*ans)

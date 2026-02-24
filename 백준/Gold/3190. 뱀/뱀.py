import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
board = [[0] * (N+1) for _ in range(N+1)]
K = int(input().strip())
for _ in range(K):
    r,c = map(int, input().split())
    board[r][c] = 2
    
L = int(input().strip())
times = {}
for _ in range(L):
    x,c = input().split()
    times[int(x)] = c

dy = [0,1,0,-1]
dx = [1,0,-1,0]

y, x = 1, 1

board[y][x] = 1
snake = deque([(y,x)])
direction = 0
time = 0

while True:
    time += 1
    ny = y + dy[direction]
    nx = x + dx[direction]

    if not (0 < ny <= N and 0 < nx <= N) or board[ny][nx] == 1:
        break
    if board[ny][nx] != 2:
        ty, tx = snake.popleft()
        board[ty][tx] = 0

    board[ny][nx] = 1
    snake.append((ny,nx))
    y,x = ny, nx

    if time in times:
        if times[time] == 'D':
            direction = (direction+1) % 4
        else:
            direction = (direction+3) % 4
print(time)
        

    
        
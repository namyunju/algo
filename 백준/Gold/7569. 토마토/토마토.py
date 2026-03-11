from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
zero = 0

for level in range(H):
    for row in range(N):
        for col in range(M):
            if boxes[level][row][col] == 1:
                q.append((level, row, col))
            elif boxes[level][row][col] == 0:
                zero += 1

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    z, x, y = q.popleft()
    for d in range(6):
        nz, nx, ny = z+dz[d], x+dx[d], y+dy[d]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = boxes[z][x][y] + 1
                q.append((nz, nx, ny))

max_day = 0
for level in range(H):
    for row in range(N):
        for col in range(M):
            if boxes[level][row][col] == 0:
                print(-1)
                sys.exit()
            max_day = max(max_day, boxes[level][row][col])

print(max_day - 1)

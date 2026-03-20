import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs(i, j):
    visited[i][j] = 1
    sub = 1
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if picture[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                    sub += 1
    return sub

count = 0
max_area = 0

for i in range(N):
    for j in range(M):
        if picture[i][j] == 1 and visited[i][j] == 0:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)
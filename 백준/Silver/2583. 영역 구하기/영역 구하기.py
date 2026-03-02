import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()

    M, N, K = map(int, input[:3])
    rects = input[3:]

    grid = [[0] * N for _ in range(M)]

    idx = 0
    for _ in range(K):
        x1, y1, x2, y2 = map(int, rects[idx:idx+4])
        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
        idx += 4

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    areas = []

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:  
                queue = deque([(i, j)])
                grid[i][j] = 1  
                count = 1
                
                while queue:
                    y, x = queue.popleft()
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
                            grid[ny][nx] = 1
                            count += 1
                            queue.append((ny, nx))
                
                areas.append(count)

    print(len(areas))
    print(*(sorted(areas)))

solve()
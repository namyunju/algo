import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve():
    grid = [list(input().strip()) for _ in range(3)]
    info = list(map(int, input().split()))
    expected_counts = sorted(info[1:])
    
    visited = [[False] * 3 for _ in range(3)]
    actual_counts = []

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'O' and not visited[i][j]:
                if i == 1 and j == 1: 
                    continue
                
                queue = deque([(i, j)])
                visited[i][j] = True
                count = 0
                
                while queue:
                    y, x = queue.popleft()
                    count += 1
                    
                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]
                        
                        if 0 <= ny < 3 and 0 <= nx < 3:
                            if grid[ny][nx] == 'O' and not visited[ny][nx]:
                                if not (ny == 1 and nx == 1):
                                    visited[ny][nx] = True
                                    queue.append((ny, nx))
                
                actual_counts.append(count)
    
    if sorted(actual_counts) == expected_counts:
        print(1)
    else:
        print(0)

t = int(input())
for _ in range(t):
    solve()
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_icebergs():
    icebergs = []
    for r in range(n):
        for c in range(m):
            if graph[r][c] > 0:
                icebergs.append((r, c))
    return icebergs

def bfs(start_r, start_c, visited):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc] > 0:
                visited[nr][nc] = True
                queue.append((nr, nc))

year = 0

while True:
    icebergs = get_icebergs()
    
    if not icebergs:
        print(0)
        break

    visited = [[False] * m for _ in range(n)]
    count = 0
    for r, c in icebergs:
        if not visited[r][c]:
            bfs(r, c, visited)
            count += 1
    
    if count >= 2:
        print(year)
        break
    
    melt_list = []
    for r, c in icebergs:
        sea_count = 0
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
                sea_count += 1
        melt_list.append((r, c, sea_count))
    
    for r, c, m_val in melt_list:
        graph[r][c] = max(0, graph[r][c] - m_val)
        
    year += 1
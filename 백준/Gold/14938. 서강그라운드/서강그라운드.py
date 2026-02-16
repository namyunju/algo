'''
수색 범위 내 아이템 총합 
'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

INF = 10**18
n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

distance = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))
    distance[a][b] = l
    distance[b][a] = l

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if distance[s][e] > distance[s][k] + distance[k][e]:
                distance[s][e] = distance[s][k] + distance[k][e]
for i in range(n+1):
    distance[i][i] = 0
ans = 0

for s_node in range(1, n+1):
    total = 0
    for i in range(1, n+1):
        if distance[s_node][i] <= m:
            total += items[i]
    ans = max(ans, total)
print(ans)
            

    
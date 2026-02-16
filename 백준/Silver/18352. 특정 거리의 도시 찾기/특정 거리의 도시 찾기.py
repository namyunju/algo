'''
X에서 출발하여 도달가능한 도시 중 최단 거리가 정확히 K인 모든 도시들의 번호를 출력
'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N,M,K,X = map(int, input().split())
INF = 10**18

dist = [INF] * (N+1)
dist[X] = 0
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

pq = []
ans = []

for node in graph[X]:
    heappush(pq, (1, node))
    dist[node] = 1
    
while pq:
    cur_dist, cur_node = heappop(pq)

    if dist[cur_node] < cur_dist:
        continue

    for nxt_node in graph[cur_node]:
        nxt_dist = cur_dist + 1
        if dist[nxt_node] > nxt_dist:
            dist[nxt_node] = nxt_dist
            heappush(pq, (nxt_dist, nxt_node))
            
for i in range(1,N+1):
    if dist[i] == K:
        ans.append(i)
        
if ans:
    for a in ans:
        print(a)
else:
    print(-1)
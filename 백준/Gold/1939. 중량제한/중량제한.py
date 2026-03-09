'''
몇 개 섬 사이 다리 
다리 중량
한 번의 이동에서 옮길 수 있는 물품 중량 최댓값
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(weight):
    queue = deque([start_node])
    visited = [False] * (N+1)
    visited[start_node] = True

    while queue:
        current = queue.popleft()

        if current == end_node:
            return True

        for nxt_node, limit in graph[current]:
            if not visited[nxt_node] and limit >= weight:
                visited[nxt_node] = True
                queue.append(nxt_node)
    return False
    

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

min_weight = 1
max_weight = 0

for _ in range(M):
    A,B,C = map(int, input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
    max_weight = max(max_weight, C)

start_node, end_node = map(int, input().split())

result = min_weight

while min_weight <= max_weight:
    mid = (min_weight + max_weight) // 2
    
    if bfs(mid):
        result = mid  
        min_weight = mid + 1
    else:
        max_weight = mid - 1 

print(result)

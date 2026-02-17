'''
먼저 푸는 것이 좋은 문제
번호가 작은 문제부터
A 풀고 B 풀어야 함
전체 푸는 순서
'''
'''
A<B이면 상관없음
A>B이면
A보다 작은 문제들 풀고 A풀고 바로 뒤에 B를 풀어야 함

위상 정렬
나보다 먼저 풀어야 하는 문제를 저 
'''
import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
    
heap = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)
        
ans = []

while heap:
    current = heapq.heappop(heap)
    ans.append(current)

    for nxt in graph[current]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)
            
print(*ans)
    
    
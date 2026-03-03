import heapq
import sys

# 입력 속도 향상
input = sys.stdin.readline
INF = float('inf')

def solve():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v, d = map(int, input().split())
        # 소수점 방지를 위해 거리에 2를 곱함
        adj[u].append((v, d * 2))
        adj[v].append((u, d * 2))

    # 1. 여우의 다익스트라 (표준 방식)
    dist_fox = [INF] * (N + 1)
    dist_fox[1] = 0
    pq = [(0, 1)]

    while pq:
        d, curr = heapq.heappop(pq)
        if dist_fox[curr] < d:
            continue
        for nxt, weight in adj[curr]:
            if dist_fox[nxt] > d + weight:
                dist_fox[nxt] = d + weight
                heapq.heappush(pq, (dist_fox[nxt], nxt))

    # 2. 늑대의 다익스트라 (상태 분리)
    # dist_wolf[node][0]: 다음에 빠르게 달릴 차례
    # dist_wolf[node][1]: 다음에 느리게 달릴 차례
    dist_wolf = [[INF] * 2 for _ in range(N + 1)]
    dist_wolf[1][0] = 0
    pq = [(0, 1, 0)] # (비용, 현재노드, 다음상태:0(fast)/1(slow))

    while pq:
        d, curr, state = heapq.heappop(pq)
        if dist_wolf[curr][state] < d:
            continue
        
        for nxt, weight in adj[curr]:
            next_state = 1 - state
            # state 0: 이번에 빠르게 달림 (가중치 / 2)
            # state 1: 이번에 느리게 달림 (가중치 * 2)
            n_weight = d + (weight // 2 if state == 0 else weight * 2)
            
            if dist_wolf[nxt][next_state] > n_weight:
                dist_wolf[nxt][next_state] = n_weight
                heapq.heappush(pq, (n_weight, nxt, next_state))

    # 3. 결과 비교
    ans = 0
    for i in range(2, N + 1):
        if dist_fox[i] < min(dist_wolf[i]):
            ans += 1
    print(ans)

solve()
'''
최소로 잃는 루피 
(0,0) 에서 시작해서 상하좌우 탐색
heap 이용해서 최소비용부터 찾고
방문한 지점 재방문 하지 않음
(N-1, N-1) 도달 시 끝
'''
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = 10**18
tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = board[0][0]

    pq = [(distance[0][0], 0, 0)]
    find = False
    while pq:
        cur_dist, x, y = heappop(pq)

        for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
            nx, ny = x + dx, y + dy
            if nx == N-1 and ny == N-1:
                print(f"Problem {tc}: {cur_dist+board[nx][ny]}")
                find = True
                break 
                
            elif 0 <= nx < N and 0 <= ny < N:
                nxt_dist = cur_dist + board[nx][ny]
                if distance[nx][ny] > nxt_dist:
                    distance[nx][ny] = nxt_dist
                    heappush(pq, (nxt_dist, nx, ny))
        
        if find:
            break

    tc += 1
    
'''
경로가 주어짐
0에서 출발하여 99에 도달 가능 여부

0에서 시작해서 연결된 노드를 넣고
방문했던 지점은 다시 안 넣고
하나씩 꺼내서 반복
'''

T = 10
for _ in range(T):
    tc, road_cnt = map(int, input().split())
    roads = list(map(int, input().split()))
    edge = [[] for _ in range(100)]

    for i in range(road_cnt):
        edge[roads[2*i]].append(roads[2*i+1])

    visited = [0] * 100

    stack = [0]
    
    ans = 0
    
    while stack:
        now = stack.pop()
        for nxt_node in edge[now]:
            if nxt_node == 99:
                ans = 1
                break
            if visited[nxt_node]:
                continue
            visited[nxt_node] = 1
            stack.append(nxt_node)
        if ans:
            break
    print(f'#{tc} {ans}')
        
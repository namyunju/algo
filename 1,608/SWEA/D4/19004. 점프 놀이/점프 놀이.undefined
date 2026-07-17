def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve():
    N, K = map(int, input().split())
    # 숫자 저장
    positions = [[] for _ in range(K+1)]
    
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            num = row[c]
            positions[num].append((r,c))
            
    for i in range(1, K+1):
        if not positions[i]:
            print(-1)
            return
    
    INF = float('inf')
    dp = {}
    
    # 숫자 1
    for r, c in positions[1]:
        dp[(r, c)] = 0
    
    for i in range(2, K+1):
        next_dp = {}
        for nr, nc in positions[i]:
            min_val = INF
            for pr, pc in positions[i-1]:
                dist = get_dist((pr, pc), (nr, nc))
                cost = dp[(pr, pc)] + dist
                if cost < min_val:
                    min_val = cost
            next_dp[(nr, nc)] = min_val
        dp = next_dp
    ans = min(dp.values())
    print(ans if ans != INF else -1)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    solve()
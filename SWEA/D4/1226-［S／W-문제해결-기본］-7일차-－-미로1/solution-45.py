import heapq

def heuristic(r, c, gr, gc):
    return abs(gr - r) + abs(gc - c)

for tc in range(1, 11):
    input()  

    maze = [list(input().strip()) for _ in range(16)]

    sr = sc = gr = gc = 0

    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                sr, sc = r, c
            elif maze[r][c] == '3':
                gr, gc = r, c

    INF = float('inf')
    dist = [[INF] * 16 for _ in range(16)]
    dist[sr][sc] = 0

    pq = []
    start_f = heuristic(sr, sc, gr, gc)

    # (f, g, r, c)
    heapq.heappush(pq, (start_f, 0, sr, sc))

    answer = 0

    while pq:
        f, g, r, c = heapq.heappop(pq)

        if g > dist[r][c]:
            continue

        if (r, c) == (gr, gc):
            answer = 1
            break

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < 16 and 0 <= nc < 16):
                continue

            if maze[nr][nc] == '1':
                continue

            ng = g + 1

            if ng < dist[nr][nc]:
                dist[nr][nc] = ng
                nf = ng + heuristic(nr, nc, gr, gc)
                heapq.heappush(pq, (nf, ng, nr, nc))

    print(f"#{tc} {answer}")
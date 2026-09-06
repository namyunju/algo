'''
가장 영향력 있는 사람.
모든 사람에게의 최종합의 숫자가 가장 작은 사람

플로이드 워셜
'''


T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]
    data = data[1:]

    INF = float('inf')

    dist = []
    idx = 0

    for i in range(N):
        row = []
        for j in range(N):
            x = data[idx]
            idx += 1

            if i == j:
                row.append(0)
            elif x == 1:
                row.append(1)
            else:
                row.append(INF)

        dist.append(row)

    for k in range(N):
        dist_k = dist[k]

        for i in range(N):
            dist_i = dist[i]
            ik = dist_i[k]

            for j in range(N):
                new_dist = ik + dist_k[j]

                if new_dist < dist_i[j]:
                    dist_i[j] = new_dist

    ans = min(map(sum, dist))

    print(f"#{tc} {ans}")
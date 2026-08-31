T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    before = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        before[b].append(a)

    visited = [False] * (N + 1)
    memo = {}

    def dfs(count):
        if count == N:
            return 1

        state = tuple(visited)

        if state in memo:
            return memo[state]

        answer = 0

        for player in range(1, N + 1):
            if visited[player]:
                continue

            possible = True

            for required in before[player]:
                if not visited[required]:
                    possible = False
                    break

            if not possible:
                continue

            visited[player] = True
            answer += dfs(count + 1)
            visited[player] = False

        memo[state] = answer
        return answer

    print(f"#{tc} {dfs(0)}")
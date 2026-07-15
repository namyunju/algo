T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tasks = []

    for _ in range(N):
        d, t = map(int, input().split())

        tasks.append((t, d))

    tasks.sort(reverse=True)

    current = float("inf")

    for deadline, duration in tasks:
        current = min(current, deadline)

        current -= duration

    print(current)
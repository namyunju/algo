import sys
sys.setrecursionlimit(1000000)

N = int(input())
MOD = 1000000

# dp[day][late][consecutive_absent]
dp = [[[-1] * 3 for _ in range(2)] for _ in range(N)]

def dfs(day, late, absent):
    if late >= 2 or absent >= 3:
        return 0

    if day == N:
        return 1

    if dp[day][late][absent] != -1:
        return dp[day][late][absent]

    count = 0

    count += dfs(day+1, late, 0)

    if late < 1:
        count += dfs(day + 1, late + 1, 0)

    if absent < 2:
        count += dfs(day + 1, late, absent + 1)

    dp[day][late][absent] = count % MOD
    return dp[day][late][absent]

print(dfs(0,0,0))
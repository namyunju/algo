N = int(input())
M = int(input())
garo = list(map(int, input().split()))
height = 1
left = garo[0]
right = N - garo[M-1]

ans = max(left, right)
for i in range(1, M):
    interval = garo[i] - garo[i-1]
    if interval%2 == 1:
        ans = max(ans, interval//2+1)
    else:
        ans = max(ans, interval//2)

print(ans)
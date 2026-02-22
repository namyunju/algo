n = int(input())
height = list(map(int, input().split()))
grow = list(map(int, input().split()))

trees = []
for i in range(n):
    trees.append((grow[i], height[i]))

trees.sort()

ans = 0
for i in range(n):
    speed, start = trees[i]
    ans += start + speed * i

print(ans)
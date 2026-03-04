import sys
input = sys.stdin.readline

n = int(input())
calls = list(map(int, input().split()))

# 30초마다 10원 추가
# 60초마다 15원 추가
y = 0
m = 0
for c in calls:
    y += (c // 30 + 1) * 10
    m += (c // 60 + 1) * 15


if y < m:
    print("Y", y)
elif m < y:
    print("M", m)
else:
    print("Y M", y)
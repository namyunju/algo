import sys
input = sys.stdin.readline 

N = int(input())
M = int(input())

friend = [set() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)

# 상근이 직접적인 친구들
my_friends = friend[1]
ans = set()

for f in my_friends:
    ans.add(f)          # 내 친구 추가
    ans.update(friend[f]) # 친구의 친구들 추가

ans.discard(1)

print(len(ans))
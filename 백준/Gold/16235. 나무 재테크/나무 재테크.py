'''
새로 생길 나무들은 나이가 1로 시작 
항상 가장 어림

나이순 정렬이 중요한 문제
가장 처음에만 정렬하고 이후 생기는 나무들은 가장 앞에 추가 appendleft
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 초기 양분은 5
ground = [[5] * N for _ in range(N)]
# 겨울에 추가되는 양분
winter = [list(map(int, input().split())) for _ in range(N)]

# 나무를 관리할 3차원 리스트 (각 칸마다 deque 생성)
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

# 처음 주어진 나무들을 나이순으로 정렬 후 deque로 변환
for i in range(N):
    for j in range(N):
        trees[i][j] = deque(sorted(trees[i][j]))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# K년 
for _ in range(K):
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                survived_trees = deque()
                dead_nutrients = 0
                # 어린 순서로
                while trees[i][j]:
                    age = trees[i][j].popleft()
                    
                    if ground[i][j] >= age:
                        ground[i][j] -= age
                        survived_trees.append(age + 1)
                        
                    else:
                        dead_nutrients += age // 2
                
                # 나무 교체, 양분
                trees[i][j] = survived_trees
                ground[i][j] += dead_nutrients

    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                # 나이가 5의 배수인 나무만 번식
                if age % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)

    for i in range(N):
        for j in range(N):
            ground[i][j] += winter[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
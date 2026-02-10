'''
2 * N 표 
첫 줄 1~N 차례로
둘째 줄 무작위 1~N

첫 줄에서 숫자 뽑으면 해당 정수들이 이루는 집합과 바로 아래 정수들 집합이 일치

최대로 많이 뽑는 방법을 찾기

뽑힌 정수의 개수 출력하고 
해당 정수들 크기순으로 하나씩 출력
'''
'''
둘쨰줄에서 어떤 수를 뽑는다면 그 숫자의 인덱스에 해당하는 숫자도
둘째줄에 존재해야함

어느 정도 연쇄적으로 순환고리가 발생해야 함
그냥 타고타고 가서 언젠가 시작점이 나오기만 하면 됨

위아래 숫자가 동일하다면 무조건 뽑기

'''
import sys
input = sys.stdin.readline
N = int(input())

second_line = [0]*(N+1)

ans = []

used = [False] * (N+1)
finished = [False] * (N+1)

for i in range(1,N+1):
    num = int(input())
    second_line[i] = num

def dfs(curr):
    used[curr] = True
    nxt = second_line[curr]

    # 사용하지 않았다면 탐색 이어나가기
    if not used[nxt]:
        dfs(nxt)

    # 사용했는데 탐색이 종료되지 않았다면
    elif not finished[nxt]:
        temp = nxt

        while temp != curr:
            ans.append(temp)
            temp = second_line[temp]
        ans.append(curr)
    finished[curr] = True
        


for i in range(1,N+1):
    if not used[i]:
        dfs(i)
        
ans.sort()
length = len(ans)
print(length)
for i in range(length):
    print(ans[i])
    
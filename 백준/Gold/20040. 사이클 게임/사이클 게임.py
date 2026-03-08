'''
싸이클 게임
두명 플레이어
선 홀수 번째 차례
후 짝수 번째 차례
평면 n 개의 점( 0~n-1 )

어느 세 점도 일직선 위에 놓이지 않고
매차례 두 점 선택하여 선분. 중복 불가, 교차 가능

싸이클 완성되는 순간 종료
사이클 C는 플레이어가 그린 선분들의 부분집합

게임 상황 주어지면 몇 번째 차례에서 사이클 완성되었는지
혹은 진행 중인지 판단하는 프로그램

'''
'''
싸이클 생성 여부 판단
유니온 파인드
더 작은 숫자를 부모로 
연결시키는데 이미 부모 같다면 싸이클 생성. 끝.

예시
0과 1, 1과 2 이어진 상태
>> 0,1,2의 부모는 0임
0과 2 잇는다면 둘의 부모 이미 같음. 종료.
'''
import sys
input = sys.stdin.readline

# x의 부모를 반환하는 함수
def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]

# 만약 이미 둘의 root가 같다면 종료 
def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return False

    if rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
    elif rank[rootB] > rank[rootA]:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA
        rank[rootA] += 1
    return True
    
        
# 점 개수, 진행 차례 수
n, m = map(int, input().split())
rank = [0] * (n)
parent = [i for i in range(n)]

def solve():
    for play in range(1,m+1):
        u,v = map(int, input().split())
        result = union(u,v)
        if not result:
            print(play)
            return 
    print(0)
solve()
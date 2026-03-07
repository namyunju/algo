'''
친구관계 그래프
두 사람 사이의 경로를 보여줌
없다면 안 보여줌


두 사람 사이의 경로 존재여부
'''
import sys 
input=sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA
    
t = int(input())
for tc in range(1,t+1):
    
    # 유저 수
    n = int(input())
    parent = [i for i in range(n)]
    # 친구 관계 수
    k = int(input())
    
    for _ in range(k):
        # a, b는 친구
        a, b = map(int, input().split())
        union(a,b)
        
    # 구할 쌍의 수
    m = int(input())
    print(f'Scenario {tc}:')
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()
        

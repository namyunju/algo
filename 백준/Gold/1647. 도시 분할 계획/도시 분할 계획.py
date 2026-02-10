import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solve():
    try:
        line1 = input().split()
        if not line1: return 
        N, M = map(int, line1)
    except ValueError: return

    edges = []
    for _ in range(M):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()

    parent = [i for i in range(N + 1)]
    
    total_cost = 0
    max_edge_cost = 0 
    edge_count = 0

    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            max_edge_cost = cost # 정렬되어 있으므로 마지막에 추가된 것이 가장 큼
            edge_count += 1
            
            if edge_count == N - 1:
                break
    
    print(total_cost - max_edge_cost)

solve()
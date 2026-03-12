import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    # 1. 트리 크기 결정 (N보다 큰 가장 가까운 2의 거듭제곱의 2배)
    # n=100,000일 때 size는 131,072가 되며, 전체 트리는 262,144 크기면 충분함
    size = 1
    while size < n:
        size *= 2
    
    # 메모리 효율을 위해 튜플 대신 각각의 리스트(배열) 사용
    min_tree = [float('inf')] * (2 * size)
    max_tree = [0] * (2 * size)
    
    # 2. 리프 노드 채우기
    for i in range(n):
        val = int(input())
        min_tree[size + i] = val
        max_tree[size + i] = val
        
    # 3. 트리 빌드 (Bottom-up)
    for i in range(size - 1, 0, -1):
        min_tree[i] = min(min_tree[i * 2], min_tree[i * 2 + 1])
        max_tree[i] = max(max_tree[i * 2], max_tree[i * 2 + 1])
        
    # 4. 쿼리 처리
    for _ in range(m):
        l, r = map(int, input().split())
        l += size - 1
        r += size - 1
        
        res_min = float('inf')
        res_max = 0
        
        while l <= r:
            if l % 2 == 1:
                res_min = min(res_min, min_tree[l])
                res_max = max(res_max, max_tree[l])
                l += 1
            if r % 2 == 0:
                res_min = min(res_min, min_tree[r])
                res_max = max(res_max, max_tree[r])
                r -= 1
            l //= 2
            r //= 2
            
        print(f"{res_min} {res_max}")

solve()
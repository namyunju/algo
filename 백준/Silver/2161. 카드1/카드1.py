from collections import deque

N = int(input())

ans = []

pq = deque(i for i in range(1, N+1))

while pq:
    first = pq.popleft()
    ans.append(first)
    if pq:
        second = pq.popleft()
        pq.append(second)
    
print(*ans)
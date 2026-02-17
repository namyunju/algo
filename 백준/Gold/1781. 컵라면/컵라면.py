'''
N개의 문제
데드라인과 컵라면

받을 수 있는 컵라면 최대 개수는?
'''
'''
컵라면 많이 주는 문제부터 해당하는 데드라인에 넣기
그 날짜에 이미 문제 있다면 더 앞 날짜로 옮기며 넣을 곳 탐색

시간초과
날짜를 하나하나 탐색하는 것 비효율적

힙 안에 있는 element의 개수 == 날짜
전체 (데드라인, 컵라면) 정렬하고 
데드라인이 작은 것부터 1번만 쭉 순회하면서
현재 힙 안에 있는 요소 개수가 데드라인보다 작다면 컵라면 수 넣어주고
아니라면 가장 작은 컵라면 개수빼고 넣기  

나중에 나오는 것일수록 데드라인 크고 컵라면도 큼
무조건 넣어주면 됨

'''
import sys
input = sys.stdin.readline
import heapq

N = int(input())
problems = []
heap = []
for i in range(N):
    dead, cup = map(int, input().split())
    problems.append((dead, cup))

problems.sort()

for dead, cup in problems:
    heapq.heappush(heap, cup)

    if len(heap) > dead:
        heapq.heappop(heap)
    
print(sum(heap))
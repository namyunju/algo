'''
두 파일을 합쳐나가 하나로 만듦
비용: 두 파일 크기의 합
최종파일 완성까지 필요한 비용의 총합은?


'''
import sys
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    ans = 0
    while files:
        if len(files) == 1:
            break
        file1 = heapq.heappop(files)
        file2 = heapq.heappop(files)
        new_file = file1 + file2
        ans += new_file
        heapq.heappush(files, new_file)
    print(ans)
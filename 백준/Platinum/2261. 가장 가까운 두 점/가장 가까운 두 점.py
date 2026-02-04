import sys
input = sys.stdin.readline

def get_dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# 분할된 점들 중 첫 점과 끝 점
def solve(start, end):

    # 총 점의 개수 
    length = end - start

    # 점이 3개 이하라면 최소 거리 계산하여 반환
    if length <= 3:
        # 최소 거리
        min_d = float('inf')
        # 서로 다른 두 점 뽑아서 거리 계산
        for i in range(start, end-1):
            for j in range(i+1, end):
                d = get_dist(points[i], points[j])
                min_d = min(min_d, d)
        return min_d

    # 분할
    # 중점의 idx
    # 중점의 x 좌표
    mid = (start + end) // 2
    mid_x = points[mid][0]

    # 좌우로 나누어서 각각 최소 거리를 구함
    d_left = solve(start, mid)
    d_right = solve(mid, end)

    # 현재까지 최소 거리
    min_d = min(d_left, d_right)

    candidates = []

    for i in range(start, end):
        # x좌표 차이의 제곱이 현재 최소 거리보다 작다면 후보군 추가
        if (points[i][0] - mid_x)**2 < min_d:
            candidates.append(points[i])

    # y좌표 고려
    candidates.sort(key=lambda x: x[1])

    c_len = len(candidates)
    for i in range(c_len-1):
        for j in range(i+1, c_len):
            dy = candidates[j][1] - candidates[i][1]
            if dy**2 >= min_d:
                break

            d = get_dist(candidates[i], candidates[j])
            min_d = min(min_d, d)
            
    return min_d

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

points.sort()

print(solve(0,n))
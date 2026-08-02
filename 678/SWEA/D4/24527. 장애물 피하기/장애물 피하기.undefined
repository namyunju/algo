'''
2차원 격자판
0,0 에서 시작
직사각형 장애물 존재 
장애물: x좌표 각각 0 이하, 0 이상 / y좌표 0 초과 (시작점보다 위쪽에 위치)

최대 k 번 이동
방문 가능한 모든 격자의 개수를 구하기
'''
'''
장애물 없을 시 방문 가능한 지점 수  

1 3 5 ... 2n-1 ) * 2 = (n/2)*(2n)*2=  2n^2
2*(n^2) + 2n + 1

여기서 장애물로 인해 방문이 불가능한 지점을 제외

y좌표가 0이하인 거는 그대로 가면 되는데
1이상인 부분에서는 장애물을 고려해야 함. 

y2 보다 위쪽에 방문 가능하려면 돌아가야 함
(x,y) 방문하려면 
왼쪽으로 돌 때 이동거리 : -x1 + 1 + y + abs(x-x1+1)
오른쪽으로 돌 때 이동거리: x2 + 1 + y + abs(x-x2-1)

>> min(-x1 + 1 + y + abs(x-x1+1), x2 + 1 + y + abs(x-x2-1))
'''
# 장애물 없을 시 방문 가능 지점 수
def diamond(k):
    return 1 + 2 * k * (k + 1)


def count_point(low, high):
    if low > high:
        return 0
    return high - low + 1


def solve(x1, x2, y1, y2, k):
    if k < y1:
        return diamond(k)

    answer = diamond(k)

    # 장애물 제거
    for x in range(x1, x2 + 1):
        max_y = k - abs(x)
        answer -= count_point(y1, min(y2, max_y))

    # 장애물 외 제외 지점
    # 장애물 돌아가기 위한 x좌표 양끝점
    left = x1 - 1
    right = x2 + 1

    for x in range(left, right + 1):
        # 장애물이 없었다면 갈 수 있는 최대 y
        normal_max_y = k - abs(x)

        # 왼쪽, 오른쪽으로 돌아가는 비용
        via_left = abs(left) + abs(x - left)
        via_right = abs(right) + abs(x - right)
        x_cost = min(via_left, via_right)

        # 우회하면 못 가기 시작하는 y
        blocked_y = k - x_cost + 1

        low = max(y2 + 1, blocked_y)
        high = normal_max_y

        answer -= count_point(low, high)

    return answer


T = int(input())

for tc in range(1, T+1):
    x1, x2, y1, y2, k = map(int, input().split())
    print(solve(x1, x2, y1, y2, k))
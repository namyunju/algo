import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    N = int(data[0])
    cranes = sorted([int(x) for x in data[1:N+1]], reverse=True)
    
    M = int(data[N+1])
    boxes = sorted([int(x) for x in data[N+2:N+2+M]], reverse=True)

    if boxes[0] > cranes[0]:
        print(-1)
        return

    time = 0
    moved_count = 0
    positions = [0] * N  
    is_moved = [False] * M 
    while moved_count < M:
        for i in range(N):
            # 현재 크레인이 탐색해야 할 위치부터 끝까지 확인
            while positions[i] < M:
                # 박스가 아직 운송되지 않았고, 현재 크레인이 들 수 있는 무게인 경우
                if not is_moved[positions[i]] and cranes[i] >= boxes[positions[i]]:
                    is_moved[positions[i]] = True
                    positions[i] += 1
                    moved_count += 1
                    break
                positions[i] += 1
        time += 1

    print(time)

solve()
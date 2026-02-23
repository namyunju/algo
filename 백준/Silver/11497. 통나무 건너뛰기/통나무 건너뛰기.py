import sys

input = sys.stdin.readline

def solve():
    line = input().strip()

    T = int(line)

    for _ in range(T):
        N = int(input().strip())
        logs = sorted(list(map(int, input().split())))

        max_diff = 0
        
        for i in range(2, N):
            diff = logs[i] - logs[i-2]
            if diff > max_diff:
                max_diff = diff
        
        print(max_diff)

solve()
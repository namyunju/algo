import sys
input = sys.stdin.readline

N,Q = map(int, input().split())

sets = [0] * (N+1)
for i in range(1, N+1):
    data = list(map(int, input().split()))
    # 크기 비교 위해
    # (크기, 집합)
    sets[i] = [data[0], set(data[1:])]
for _ in range(Q):
    command = list(map(int, input().split()))

    if command[0] == 1:
        set1_len = sets[command[1]][0]
        set1 = sets[command[1]][1]
        set2_len = sets[command[2]][0]
        set2 = sets[command[2]][1]

        if set1_len >= set2_len:
            set1.update(set2)
            
            sets[command[1]][0] = len(set1)
            sets[command[1]][1] = set1
            sets[command[2]][0] = 0
            sets[command[2]][1] = set()
            
        else:
            set2.update(set1)
            sets[command[1]][0] = len(set2)
            sets[command[1]][1] = set2
            sets[command[2]][0] = 0
            sets[command[2]][1] = set()
    else:
        print(sets[command[1]][0])
    
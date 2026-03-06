import sys

def solve():
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    
    room = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    cleaned_count = 0
    
    while True:
        if room[r][c] == 0:
            room[r][c] = 2  
            cleaned_count += 1
            
        cleanable = False
        
        for _ in range(4):
            d = (d - 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                r, c = nr, nc  
                cleanable = True
                break
                
        if not cleanable:
            back_d = (d + 2) % 4
            nr = r + dr[back_d]
            nc = c + dc[back_d]
            
            if room[nr][nc] == 1:
                break
            else:
                r, c = nr, nc
                
    print(cleaned_count)

solve()
import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
    
squares = []
    
for i in range(1, 101):
    num = i * i
    if m <= num <= n:
        squares.append(num)
            
if not squares:
    print(-1)
else:
    print(sum(squares))
    print(min(squares))

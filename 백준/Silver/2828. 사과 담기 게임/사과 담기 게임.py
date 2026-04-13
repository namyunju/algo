import sys

input = sys.stdin.readline

n, m = map(int, input().split())

j = int(input())


left = 1
right = m
distance = 0

for _ in range(j):
    pos = int(input())

    
    if pos > right:
        move = pos - right
        distance += move
        right = pos
        left += move

        
    elif pos < left:
        move = left - pos
        distance += move
        left = pos
        right -= move
        
print(distance)
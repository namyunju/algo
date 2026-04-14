import sys

s = int(sys.stdin.readline())

n = 1
total = 0

while True:
    total += n
    if total > s:
        break
    n += 1

print(n - 1)
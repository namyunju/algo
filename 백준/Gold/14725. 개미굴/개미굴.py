import sys
from collections import defaultdict

input = sys.stdin.readline

# 트라이 Trie 구조
# 자기 자신을 기본값으로 반환하는 함수. 무한중첩 딕셔너리
def trie():
    return defaultdict(trie)

cave = trie()

def print_trie(curr_node, depth):
    for key in sorted(curr_node.keys()):
        print("--" * depth + key)
        print_trie(curr_node[key], depth+1)
        
N = int(input())
for _ in range(N):
    data = input().split()
    # 먹이 정보 개수
    k = int(data[0])
    # 먹이 경로
    foods = data[1:]

    curr = cave

    for food in foods:
        curr = curr[food]
print_trie(cave, 0)
    
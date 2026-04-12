'''
각 자리별로 다수인 문자를 따라감
다른 문자 개수만큼 +

ACGT

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna_list = [input().strip() for _ in range(N)]

ans = ''
dist = 0

for char_idx in range(M):
    cnt = {'A':0, 'C':0, 'G':0, 'T':0}
    for dna_idx in range(N):
        cnt[dna_list[dna_idx][char_idx]] += 1

    sub_ans = ''
    sub_dist = 0
    for key in cnt:
        if cnt[key] > sub_dist:
            sub_ans = key
            sub_dist = cnt[key]

    ans += sub_ans
    dist += (N-sub_dist)

print(ans)
print(dist)
            
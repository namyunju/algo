words = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)

    count = [0] * 10
    arr = input().split()

    for word in arr:
        count[words.index(word)] += 1

    result = []

    for i in range(10):
        for _ in range(count[i]):
            result.append(words[i])

    print(tc, ' '.join(result))
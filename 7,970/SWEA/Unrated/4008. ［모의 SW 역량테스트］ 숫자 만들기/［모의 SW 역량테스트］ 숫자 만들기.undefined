def calculate(plus, minus, mul, div, cur, idx):
    global max_num, min_num, N
    if (plus == minus == mul == div == 0):
        if (cur > max_num):
            max_num = cur
        if (cur < min_num):
            min_num = cur
        return

    if plus:
        calculate(plus - 1, minus, mul, div, cur + nums[idx], idx + 1)
    if minus:
        calculate(plus, minus - 1, mul, div, cur - nums[idx], idx + 1)
    if mul:
        calculate(plus, minus, mul - 1, div, cur * nums[idx], idx + 1)
    if div:
        calculate(plus, minus, mul, div - 1, int(cur / nums[idx]), idx + 1)
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ops= list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_num = -float('inf')
    min_num = float('inf')

    calculate(ops[0], ops[1], ops[2], ops[3], nums[0], 1)
    ans = max_num - min_num
    print(f'#{tc} {ans}')
    
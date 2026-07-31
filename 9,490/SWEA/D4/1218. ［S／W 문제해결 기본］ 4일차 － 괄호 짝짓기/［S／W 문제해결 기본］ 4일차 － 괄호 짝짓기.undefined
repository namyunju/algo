def solve():
    length = int(input())
    gwalho = input()
    
    stack = []
    open_gwal = ['(', '{', '[', '<']
    close_gwal = [')', '}', ']', '>']
    
    for i in range(length):
        if (gwalho[i] in open_gwal):
            stack.append(gwalho[i])
        else:
            idx = close_gwal.index(gwalho[i])
            if stack:
                if (stack[-1] == open_gwal[idx]):
                    stack.pop()
                else:
                    return 0
            else:
                return 0
    return 1
                
for tc in range(1,11):
    ans = solve()
    print(f'#{tc} {ans}')
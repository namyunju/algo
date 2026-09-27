'''
8개의 숫자 암호코드
숫자하나는 7개의 비트로 
>> 암호코드 가로 길이는 56

올바른 암호코드인지 판별
'''
'''
각 행을 뒤쪽 열에서부터 순회
7개씩 끊어서 
숫자 확인
'''

code_to_num = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    password_line = ""

    for _ in range(N):
        line = input().strip()

        if "1" in line:
            password_line = line

    end_idx = M
    for idx in range(M-1, -1, -1):
        if password_line[idx] == "1":
            end_idx = idx
            break

    password = password_line[end_idx - 55 : end_idx+1]

    numbers = []

    for i in range(0, 56, 7):
        bit = password[i : i+7]
        numbers.append(code_to_num[bit])

    odd_sum = numbers[0] + numbers[2] + numbers[4] + numbers[6]
    even_sum = numbers[1] + numbers[3] + numbers[5] + numbers[7]

    check = odd_sum * 3 + even_sum

    if check % 10 == 0:
        ans = sum(numbers)

    else:
        ans = 0

    print(f'#{tc} {ans}')
        

            
import sys

def solve():
    # 입력 처리
    cards = []
    colors = []
    
    # 5장의 카드를 입력받아 숫자와 색상을 분리 저장
    for _ in range(5):
        line = sys.stdin.readline().split()
        color = line[0]
        num = int(line[1])
        colors.append(color)
        cards.append(num)

    # 숫자를 정렬해야 스트레이트 판별과 최댓값 찾기가 쉬움
    cards.sort()
    
    # 숫자 빈도수 체크 (인덱스 1~9 사용)
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1

    # 공통 상태 판별
    # 1. 플러시 여부: 색상의 종류가 1개인가?
    is_flush = (len(set(colors)) == 1)
    
    # 2. 스트레이트 여부: 연속된 5개의 숫자인가?
    # 정렬된 상태이므로 각 인덱스의 값과 첫 값+인덱스가 일치하는지 확인하거나
    # 단순히 4번 반복하며 앞뒤 차이가 1인지 확인
    is_straight = True
    for i in range(4):
        if cards[i] + 1 != cards[i+1]:
            is_straight = False
            break

    # 우선순위대로 점수 반환
    # 1. 스트레이트 플러시 (900 + 가장 큰 수)
    if is_flush and is_straight:
        return 900 + cards[4]

    # 2. 포카드 (800 + 같은 수)
    if 4 in cnt:
        return 800 + cnt.index(4)

    # 3. 풀하우스 (700 + 3장숫자*10 + 2장숫자)
    if 3 in cnt and 2 in cnt:
        return 700 + cnt.index(3) * 10 + cnt.index(2)

    # 4. 플러시 (600 + 가장 큰 수)
    if is_flush:
        return 600 + cards[4]

    # 5. 스트레이트 (500 + 가장 큰 수)
    if is_straight:
        return 500 + cards[4]

    # 6. 트리플 (400 + 같은 수)
    if 3 in cnt:
        return 400 + cnt.index(3)

    # 7. 투 페어 (300 + 큰수*10 + 작은수)
    # cnt 배열에 2가 2개 있어야 함
    if cnt.count(2) == 2:
        pairs = []
        for i in range(1, 10):
            if cnt[i] == 2:
                pairs.append(i)
        # pairs는 오름차순으로 들어감 (cnt 인덱스 순회하므로)
        return 300 + pairs[1] * 10 + pairs[0]

    # 8. 원 페어 (200 + 같은 수)
    if 2 in cnt:
        return 200 + cnt.index(2)

    # 9. 탑 (100 + 가장 큰 수)
    return 100 + cards[4]

# 결과 출력
print(solve())
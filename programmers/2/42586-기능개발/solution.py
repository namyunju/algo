'''
여러 기능 개발 
뒤에 있는 기능이 앞 기능보다 먼저 개발될 수 있지만 배포는 앞에 있는 기능과 함께 배포

작업 진도 배열 progresses
작업 속도 speeds
각 배포마다 배포되는 기능 개수를 return

1. 작업별 소요 일자 계산
2. 앞에서부터 최댓값 갱신 
3. 갱신된 인덱스 차이만큼 배포됨
'''
import math

def solution(progresses, speeds):
    N = len(progresses)
    work_days = [100] * N
    for i in range(N):
        work_days[i] = math.ceil((work_days[i] - progresses[i]) / speeds[i])
    
    ans = []
    
    max_idx = 0
    max_num = work_days[0]
    
    for j in range(N):
        if work_days[j] > max_num:
            max_num = work_days[j]
            ans.append(j-max_idx)
            max_idx = j
    
    ans.append(N-max_idx)
    
    return ans
    

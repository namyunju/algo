import sys
input = sys.stdin.readline

def merge_sort(start, end):
    global result
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        
        # 병합 과정
        temp = []
        i, j = start, mid + 1
        
        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                # 오른쪽 원소가 더 작을 때: 왼쪽 그룹에 남은 개수만큼 swap 발생
                temp.append(arr[j])
                result += (mid - i + 1)
                j += 1
        
        # 남은 원소 처리
        if i <= mid:
            temp.extend(arr[i:mid+1])
        if j <= end:
            temp.extend(arr[j:end+1])
            
        # 원래 배열에 덮어쓰기
        for k in range(len(temp)):
            arr[start + k] = temp[k]

n = int(input())
arr = list(map(int, input().split()))
result = 0

merge_sort(0, n - 1)
print(result)
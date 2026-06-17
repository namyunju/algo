def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
    
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    
    return answer
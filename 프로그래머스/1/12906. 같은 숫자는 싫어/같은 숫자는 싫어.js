function solution(arr)
{
    const answer = [];

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for (let i = 0; i< arr.length; i++) {
        if (arr[i] !== arr[i+1]) {
            answer.push(arr[i]);
        }
    }
    
    return answer;
}
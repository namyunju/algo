/*
총 N일 중 X기간 최다 방문한 시점

최다 방문자 수 및 해당 기간 개수 출력
*/
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X;
    cin >> N >> X;
    
    vector<int> visitor(N);
    for (int i=0; i<N; i++) {
        cin >> visitor[i];
    }

    int ansCnt=1;
    // 구간합
    // 1일부터 X일까지로 시작
    int partialSum = accumulate(visitor.begin(), visitor.begin()+X,0);
    int ansSum = partialSum;
    
    // 한 칸씩 뒤로 밀면서
    // 총 방문자수 체크
    // 최대 방문자 수 바뀌면 답 갱신
    for (int i=X; i<N; i++) {
        partialSum -= visitor[i-X];
        partialSum += visitor[i];

        if (partialSum > ansSum) {
            ansSum = partialSum;
            ansCnt = 1;
        } else if (partialSum == ansSum) {
            ansCnt++;
        }
    }

    if (ansSum != 0) {
        cout << ansSum << "\n" << ansCnt;
        return 0;
    }
    cout << "SAD";

    return 0;
}
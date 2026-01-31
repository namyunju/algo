// 기차 내 최다 인원 수
// 10개의 정차역
// 내리고 탐
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int cnt = 0;
    int ans = 0;
    
    int inCnt, outCnt;

    for (int i=0; i<10; i++) {
        cin >> outCnt >> inCnt;
        cnt -= outCnt;
        cnt += inCnt;

        if (cnt > ans) {
            ans = cnt;
        }
        
    }

    cout << ans;
    
    return 0;
}
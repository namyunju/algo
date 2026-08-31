#include <iostream>
using namespace std;

// point
// 정렬 가능한 행렬이 주어짐
// 뒤집기는 반드시 1행을 포함
int arr[65][65];

void solve() {
    int N;
    cin >> N;
    
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> arr[i][j];
        }
    }
    // 뒤집기 횟수
    int flip = 0;
    // 큰 정사각형부터 작은 정사각형까지
    for (int k=N; k>=2; k--) {
        int sort_val = k;
        int cur_val = arr[0][k-1];
        
        if (flip % 2 == 1) {
            cur_val = arr[k-1][0];
        }
        
        if (cur_val != sort_val) {
            flip++;
        }
    }
    cout << flip << "\n";
}

int main() {
    int T;
    cin >> T;
    
    while (T--) {
        solve();
    }
    return 0;
}
        
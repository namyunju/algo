#include <iostream>
#include <vector>

using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, B;
    cin >> A >> B;

    // 정수를 담을 벡터
    vector<int> sequence;
    // 0번 인덱스는 비우고 1번부터 시작
    sequence.push_back(0);

    // sequence에 i를 i번 넣기
    for (int i=1; sequence.size()<=1000; i++) {
        for (int j=0; j<i; j++) {
            if (sequence.size() > 1000) break;
            sequence.push_back(i);
        }
    }

    int ans = 0;
    for (int i=A; i<=B; i++) {
        ans += sequence[i];
    }
    cout << ans;
    return 0;
}
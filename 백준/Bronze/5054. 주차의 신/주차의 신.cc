#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


void solve() {
    int n;
    cin >> n;
    
    int min_pos = 100; 
    int max_pos = -1;  
    
    for (int i = 0; i < n; ++i) {
        int pos;
        cin >> pos;
        
        if (pos < min_pos) min_pos = pos;
        if (pos > max_pos) max_pos = pos;
    }
    
    cout << (max_pos - min_pos) * 2 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
    return 0;
}
#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++)
        {
            int N;
            cin >> N;

            // 기본 priority_queue 는 최대 힙
            priority_queue<int> pq;

            cout << "#" << tc;
            
            for (int i = 0; i < N; i++)
                {
                    int command;
                    cin >> command;

                    if (command == 1)
                    {
                        int x;
                        cin >> x;
                        pq.push(x);
                    }
                    else
                    {
                        if (pq.empty())
                        {
                            cout << " " << -1;
                        }
                        else{
                            cout << " " << pq.top();
                            pq.pop();
                        }
                    }
                }
            cout << "\n";
        }
    return 0;
}
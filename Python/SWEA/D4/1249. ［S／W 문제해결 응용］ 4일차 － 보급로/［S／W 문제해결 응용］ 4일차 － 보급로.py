/*
칸마다 복구 시간이 존재. 
모든 비용이 1이라면 BFS를 사용 가능하지만 비용이 다르므로 다익스트라를 사용

dist[][]로 칸별 도달 위한 최소 비용을 저장
priority_queue로 비용이 작은 위치부터 처리
*/

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

const int INF = 987654321;

int N;
int mapArr[100][100];
int distArr[100][100];

// 상 하 좌 우
int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

void dijkstra()
{
    // 초기 거리 설정
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N;  x++) {
            distArr[y][x] = INF;
        }
    }
    // {비용, {y, x}}
    priority_queue<
        pair<int, pair<int, int>>,
        vector<pair<int, pair<int, int>>>,
        greater<pair<int, pair<int, int>>>
    > pq;
    
    distArr[0][0] = 0;
    pq.push({0, {0, 0}});
    
    while (!pq.empty()) {
        int currentCost = pq.top().first;
        int y = pq.top().second.first;
        int x = pq.top().second.second;
        
        pq.pop();
        
        if (currentCost > distArr[y][x])
            continue;
        
        for (int dir = 0; dir < 4; dir++) {
            int ny = y + dy[dir];
            int nx = x + dx[dir];
            
            if (ny < 0 || ny >= N || nx < 0 || nx >= N)
                continue;
            
            int nextCost = currentCost + mapArr[ny][nx];
            
            if (nextCost < distArr[ny][nx]) {
                distArr[ny][nx] = nextCost;
                pq.push({nextCost, {ny, nx}});
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    for (int tc = 1; tc <= T; tc++) {
        cin >> N;
        // 복구시간 입력받음. 문자열로 받고 숫자로 전환.
        for (int y = 0; y < N; y++) {
            string input;
            cin >> input;
            
            for (int x = 0; x < N; x++) {
                mapArr[y][x] = input[x] - '0';
            }
        }
        dijkstra();
        cout << "#" << tc <<" " << distArr[N-1][N-1] << '\n';
    }
    return 0;
}
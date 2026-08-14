/*
사다리
출발점 찾기
2에서 시작해서 1을 따라 올라감.
올라가던 중 현 위치 기준으로 좌, 우를 봤을 때 길이 있다면 해당 방향으로 이동
좌, 우로 이동하던 중 위로 올라가는 길이 있다면 위로 올라감
위로 올라가던 중 Y가 0이 되면 해당 지점의 X가 답
*/
import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int [] dy = {0, 0, -1};
        int [] dx = {-1, 1, 0};

        for (int tc = 1; tc <= 10; tc++) {
            int t = Integer.parseInt(br.readLine());
            int[][] ladder = new int[100][100];
            int[][] visited = new int[100][100];

            for (int y = 0; y < 100; y++){
                StringTokenizer st = new StringTokenizer(br.readLine());

                for(int x = 0; x <100; x++){
                    ladder[y][x] = Integer.parseInt(st.nextToken());
                }
            }

            // 도착지점 (2) 찾기
            int curr_x = 0;
            int curr_y = 99;

            for (int x = 0; x < 100; x++) {
                if (ladder[99][x] == 2) {
                    curr_x = x;
                    visited[99][x] = 1;
                    break;
                }
            }

            // 찾았으면 올라가기
            while (curr_y != 0) {
                for (int d = 0; d < 3; d++) {
                    int nxt_x = curr_x + dx[d];
                    int nxt_y = curr_y + dy[d];

                    if ((0 <= nxt_x) && ( nxt_x <= 99) && (0 <= nxt_y) && (nxt_y <= 99) && (visited[nxt_y][nxt_x] != 1)) {
                        if (ladder[nxt_y][nxt_x] == 1) {
                            curr_x = nxt_x;
                            curr_y = nxt_y;
                            visited[nxt_y][nxt_x] = 1;
                            break;
                        }
                    }
                }
            }
            sb.append("#").append(tc).append(" ").append(curr_x).append("\n");
        }
        System.out.print(sb);
    }
}
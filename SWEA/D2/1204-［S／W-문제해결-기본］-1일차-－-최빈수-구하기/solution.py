import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; i++) {
            int tc = Integer.parseInt(br.readLine());

            int[] scoreCount = new int[101];

            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 1000; j++) {
                int score = Integer.parseInt(st.nextToken());
                scoreCount[score]++;
            }

            int ans = 0;
            int cnt = 0;
            for (int k = 0; k <= 100; k++) {
                if (scoreCount[k] >= cnt) {
                    cnt = scoreCount[k];
                    ans = k;
                }
            }

            sb.append("#").append(tc).append(" ").append(ans).append("\n");
        }
        System.out.print(sb);


    }
}
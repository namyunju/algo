import java.util.*;
import java.io.*;

public class Solution {

    public static void main(String[] args) throws Exception {

        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {

            StringTokenizer st = new StringTokenizer(br.readLine());

            String S1 = st.nextToken();
            String S2 = st.nextToken();

            int[] S1Cnt = new int[26];
            int[] S2Win = new int[26];

            int cnt = 0;

            if (S2.length() < S1.length()) {
                sb.append('#')
                  .append(tc)
                  .append(' ')
                  .append(0)
                  .append('\n');

                continue;
            }

            // S1의 문자 개수와 S2의 첫 번째 윈도우 설정
            for (int i = 0; i < S1.length(); i++) {
                S1Cnt[S1.charAt(i) - 'a']++;
                S2Win[S2.charAt(i) - 'a']++;
            }

            // 첫 번째 윈도우 확인
            if (Arrays.equals(S1Cnt, S2Win)) {
                cnt++;
            }

            // 슬라이딩 윈도우
            for (int i = S1.length(); i < S2.length(); i++) {

                // 새로 들어오는 문자 추가
                S2Win[S2.charAt(i) - 'a']++;

                // 윈도우에서 빠지는 문자 제거
                S2Win[S2.charAt(i - S1.length()) - 'a']--;

                if (Arrays.equals(S1Cnt, S2Win)) {
                    cnt++;
                }
            }

            sb.append('#')
              .append(tc)
              .append(' ')
              .append(cnt)
              .append('\n');
        }

        System.out.print(sb);
    }
}
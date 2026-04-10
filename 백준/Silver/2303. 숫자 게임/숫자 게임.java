import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

// The main method must be in a class named "Main".
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 최대점수
        int maxScore = -1;
        int winner = 0;

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] cards = new int[5];
            for (int j = 0; j <5; j++) {
                cards[j] = Integer.parseInt(st.nextToken());
            }
            int currentMax = 0;

            for (int a = 0; a < 3; a++) {
                for (int b = a + 1; b < 4; b++) {
                    for (int c = b + 1; c < 5; c++) {
                        int sum = cards[a] + cards[b] + cards[c];
                        int digit = sum % 10;
                        currentMax = Math.max(currentMax, digit);
                    }
                }
            }

            if (currentMax >= maxScore) {
                maxScore = currentMax;
                winner = i;
            }
        }
        System.out.println(winner);
    }
}
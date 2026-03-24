import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] trees = new Integer[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(trees, Collections.reverseOrder());
        int maxDay = 0;

        for (int i=0; i<N; i++) {
            int finishDay = (i+1) + trees[i];
            if (finishDay > maxDay) {
                maxDay = finishDay;
            }
        }
        System.out.println(maxDay+1);
    }
}
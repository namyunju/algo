import java.util.Scanner;

// n명
// 본인보다 왼쪽에 큰 사람 얼마나 있는가
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] result = new int[n];

        for (int i=0; i<n; i++) {
            int leftCount = sc.nextInt();
            int count = 0;

            for (int j=0; j<n; j++) {
                if (result[j] == 0) {
                    if (count == leftCount) {
                        result[j] = i+1;
                        break;
                    }
                    count++;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int val : result) {
            sb.append(val).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
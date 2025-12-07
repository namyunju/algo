import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();

        }
        // Please write your code here.
        int now = arr[0];
        int cnt = 1;
        int ans = 1;

        for (int j=1; j<n; j++) {
            if (now == arr[j]) {
                cnt += 1;
                if (ans < cnt) {
                    ans = cnt;
                }
            } else {
                now = arr[j];
                cnt = 1;
            }
        }
        System.out.print(ans);
    }
}
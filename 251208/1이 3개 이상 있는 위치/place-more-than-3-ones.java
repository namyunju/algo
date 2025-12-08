import java.util.Scanner;
public class Main {
    public static boolean inRange(int a, int b, int s) {
        return ((0<=a)&&(a<s)&&(0<=b)&&(b<s));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        // Please write your code here.
        int ans = 0;
        int cnt = 0;
        int[] dx = new int[] {1,0,-1,0};
        int[] dy = new int[] {0,-1,0,1};

        for (int i=0;i<n;i++) {
            for (int j=0; j<n; j++) {
                cnt = 0;
                for (int k=0; k<4;k++) {
                    if (inRange(i+dx[k], j+dy[k], n) && (arr[i+dx[k]][j+dy[k]] == 1)) {
                        cnt++;
                    }
                }
                if (cnt >= 3) {
                    ans++;
                }

            }
        }
        System.out.print(ans);
    }
}
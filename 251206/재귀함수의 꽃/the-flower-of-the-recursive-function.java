import java.util.Scanner;
public class Main {
    public static void solve(int N) {
        if (N==0) {
            return;
        }
        System.out.print(N + " ");
        solve(N-1);
        System.out.print(N+" ");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        solve(n);
    }
}
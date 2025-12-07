import java.util.Scanner;
public class Main {
    public static void solve(int a, int b, int c, int d) {
        int ans= 0;

        if (b != d) {
            ans += (60-b);
            ans += d;
            a += 1;
        }
        
        if (a != c) {
            ans += (c-a)*60;
        }

        System.out.print(ans);
       
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        // Please write your code here.
        solve(a,b,c,d);
    }
}
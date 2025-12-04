import java.util.Scanner;
public class Main {
    public static void solve(int a, int b) {
        if (a<b) {
            a += 10;
            b *=2;
            System.out.print(a + " " + b);
        } else {
            a *= 2;
            b += 10;
            System.out.print(a + " " + b);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        // Please write your code here.
        solve(a,b);
    }
}
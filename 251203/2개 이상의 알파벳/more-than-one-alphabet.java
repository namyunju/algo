import java.util.Scanner;
public class Main {
    public static void solve(String str) {
        int len = str.length();
        char first = str.charAt(0);
        for (int i=1; i<len; i++) {
            if (first != str.charAt(i)) {
                System.out.print("Yes");
                return;
            }
        }
        System.out.print("No");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        // Please write your code here.
        solve(A);
    }
}
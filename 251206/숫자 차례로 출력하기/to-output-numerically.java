import java.util.Scanner;
public class Main {
    public static void func1(int N) {
        if (N==0) {
            return;
        }
        func1(N-1);
        System.out.print(N+" ");
    }
    public static void func2(int N) {
        if (N == 0) {
            return;
        }
        System.out.print(N+" ");
        func2(N-1);

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        func1(n);
        System.out.println();
        func2(n);
    }
}
import java.util.Scanner;
public class Main {
    public static void star(int N) {
        if (N==0) {
            return;
        }
        for (int i=0; i<N; i++) {
            System.out.print("* ");
        }
        System.out.println();
        star(N-1);
        for (int i=0; i<N; i++) {
            System.out.print("* ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        star(n);
    }
}
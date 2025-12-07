import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] lines = new int[201];

        for (int i=0; i<N; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            s += 100;
            e += 100;
            for (int j=s; j<e; j++) {
                lines[j] += 1;
            }
        }

        int max = 0;
        for (int x : lines) {
            max = Math.max(max, x);
        }
        System.out.print(max);
    }
}
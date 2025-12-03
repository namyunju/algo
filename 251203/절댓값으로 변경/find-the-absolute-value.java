import java.util.Scanner;

public class Main {
    public static void solve(int[] numbers, int N) {
        for (int i=0; i<N; i++) {
            if (numbers[i] <0) {
                System.out.print(-numbers[i] + " ");
            } else {
                System.out.print(numbers[i] + " ");
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // Please write your code here.
        solve(arr, n);
    }
}
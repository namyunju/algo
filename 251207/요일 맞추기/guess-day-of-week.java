import java.util.Scanner;

public class Main {
    static final String[] days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
    static final int[] num_days = {0,31,28,31,30,31,30,31,31,30,31,30,31};

    public static void solve(int m1, int d1, int m2, int d2) {
        int diff = 0;

        if (m1 == m2) {
            diff = d2 - d1;
        } else if (m1 < m2) {
            diff += num_days[m1] - d1;        // 첫 달 남은 날짜
            for (int i = m1 + 1; i < m2; i++) // 중간 달
                diff += num_days[i];
            diff += d2;                       // 마지막 달 날짜
        } else { // m1 > m2
            diff -= d1;                        // 첫 달 지나간 날짜
            for (int i = m1 - 1; i > m2; i--)  // 중간 달
                diff -= num_days[i];
            diff -= (num_days[m2] - d2);       // 마지막 달 남은 날짜
        }

        // 요일은 7로 나눠 정규화
        int idx = ((diff % 7) + 7) % 7;

        System.out.print(days[idx]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();

        solve(m1, d1, m2, d2);
        sc.close();
    }
}

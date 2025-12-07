import java.util.Scanner;
public class Main {
    public static void solve(int m1, int d1, int m2, int d2) {
        int day = 0;
        String[] days = new String[] {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
        int[] num_days = new int[] {0,31,28,31,30,31,30,31,31,30,31,30,31};
        String ans;
        if (m1 == m2) {
            if (d1 >= d2) {
                day = (d1-d2)%7;
                if (day == 0) {
                    ans = days[day];
                    System.out.print(ans);
                } else {
                    ans = days[7-day];
                    System.out.print(ans);
                }
                return;

            } else {
                day = (d2-d1)%7;
                ans = days[day];
                System.out.print(ans);
                return;
            }
        } else if (m1 < m2) {
            day += num_days[m1] - d1;
            for (int i=m1+1; i<m2-1; i++) {
                day += num_days[i];
            }
            day += d2;
        } else {
            day += d1;
            for (int i=m1-1; i>m2; i--) {
                day += num_days[i];
            }
            day += num_days[m2]-d2;
        }
        day %= 7;
        if (day == 0) {
        ans = days[day];

        } else {
            ans = days[7-day];
        }

        System.out.print(ans);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        // Please write your code here.
        solve(m1,d1,m2,d2);
    }
}
import java.util.Scanner;

// 15라면 한 자리수 9개, 두 자리수 6개
// 115라면 한 자리수 9개, 두 자리수 10~99 90개, 세 자리수 100~115 16개
// 1234라면 한 자리수 9개, 두 자리수 10~99 90개, 세 자리수 100~999 900개, 네 자리수 1000~1234 235개

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextInt();
        String str = String.valueOf(N);
        int length = str.length();

        int cnt = 1;
        int ans = 0;

        while (cnt < length) {
            ans += (9 * Math.pow(10, (cnt-1)))*cnt;
            cnt++;
        }
        ans += (N-Math.pow(10,cnt-1)+1)*(cnt);
        System.out.println(ans);
        
    }
}
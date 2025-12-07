import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        // 매초별 a와 b의 위치를 기록

        int[] loca = new int[1000000];
        int[] locb = new int[1000000];

        // A 이동 방향, 시간 
        int nowa = 0;
        int timea = 0;
        for (int i=0; i<n; i++) {
            String da = sc.next();
            int sa = sc.nextInt();

            for (int j=0; j<sa; j++) {
                timea +=1 ;
                if (da.equals("R")) {
                    nowa += 1;
                    loca[timea] = nowa;
                } else {
                    nowa -= 1;
                    loca[timea] = nowa;
                }
            }
        }
        int nowb = 0;
        int timeb = 0;
        for (int i=0; i < m; i++) {
            String db = sc.next();
            int sb = sc.nextInt();
            for (int j=0; j<sb; j++) {
                timeb += 1;
                if (db.equals("R")) {
                    nowb++;
                    locb[timeb] = nowb;
                } else {
                    nowb--;
                    locb[timeb] = nowb;
                }
            }
        }
        // Please write your code here.
        int ans = -1;
        for (int k=1; k<=timeb; k++) {
            if (loca[k] == locb[k]) {
                ans = k;
                break;
            }
        }
        System.out.print(ans);
    }
}
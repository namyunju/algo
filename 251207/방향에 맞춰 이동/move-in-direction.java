import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int x = 0;
        int y = 0;
        // 서 북 동 남 
        int[] dx = new int[] {1,0,-1,0};
        int[] dy = new int[] {0,1,0,-1};

        int N = sc.nextInt();
        for (int i=0; i<N; i++) {
            String dir = sc.next();
            int norm = sc.nextInt();

            if (dir.equals("N")) {
                x += dx[1]*norm;
                y += dy[1]*norm;
            } else if (dir.equals("S")) {
                x += dx[3]*norm;
                y += dy[3]*norm;
            } else if (dir.equals("W")) {
                x += dx[2]*norm;
                y += dy[2]*norm;
            } else {
                x += dx[0]*norm;
                y += dy[0]*norm;
            }
        }
        System.out.print(x + " " + y);
    }
}
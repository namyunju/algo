import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        // Please write your code here.
        int len = s.length();

        int x =0, y=0;
        int dirNum = 0;
        // 북 왼 남 오
        int[] dx = new int[] {0,-1,0,1};
        int[] dy = new int[] {1,0,-1,0};
        
        for (int i = 0; i<len; i++) {
            char command = s.charAt(i);
            if (command =='L') {
                dirNum++;
                dirNum %=4;
            } else if (command =='R') {
                dirNum--;
                dirNum+=4;
                dirNum%=4;
            } else {
                x += dx[dirNum];
                y += dy[dirNum];
            }
        }
        System.out.print(x + " " + y);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] map = new int[101][101]; 
        int totalArea = 0;

        for (int i=0; i<4; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            for (int x = x1; x < x2; x++) {
                for (int y=y1; y<y2; y++) {
                    map[x][y] = 1;
                }
            }
        }
        for (int i=0; i<=100; i++) {
            for (int j=0; j<100; j++) {
                if (map[i][j] == 1) {
                    totalArea++;
                }
            }
        }
        System.out.println(totalArea);
        sc.close();
    }
}
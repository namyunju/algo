import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        char[][] castle = new char[N][M];
        for (int i=0; i<N; i++) {
            String line = sc.next();
            for (int j=0; j<M; j++) {
                castle[i][j] = line.charAt(j);
            }
        }
        int rowCount = 0;
        for (int i=0; i<N; i++) {
            boolean hasGuard = false;
            for (int j=0; j<M; j++) {
                if (castle[i][j] == 'X') {
                    hasGuard = true;
                    break;
                }
            }
            if (!hasGuard) rowCount++;
        }
        int colCount = 0;
        for (int j=0; j<M; j++) {
            boolean hasGuard = false;
            for (int i=0; i<N; i++) {
                if (castle[i][j] == 'X') {
                    hasGuard = true;
                    break;
                }
            }
            if (!hasGuard) colCount++;
        }
        System.out.println(Math.max(rowCount, colCount));
    }
}
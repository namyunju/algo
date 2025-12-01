import java.util.Scanner;
class Bomb {
    String solveCode;
    char lineColor;
    int exactSec;

    public Bomb(String solveCode, char lineColor, int exactSec) {
        this.solveCode = solveCode;
        this.lineColor = lineColor;
        this.exactSec = exactSec;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String uCode = sc.next();
        char lColor = sc.next().charAt(0);
        int time = sc.nextInt();
        // Please write your code here.
        Bomb bomb1 = new Bomb(uCode, lColor, time);
        System.out.println("code : " + bomb1.solveCode);
        System.out.println("color : " + bomb1.lineColor);
        System.out.println("second : " + bomb1.exactSec);
    }
}
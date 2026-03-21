import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = 3;
        for (int t=0; t<tc; t++) {
            int N = sc.nextInt();
            BigInteger sub = BigInteger.ZERO;
            for (int i=0; i<N; i++) {
                BigInteger a = sc.nextBigInteger();
                sub = sub.add(a);
            }
            int signal = sub.signum();
            if (signal < 0) {
                System.out.println("-");
            } else if (signal > 0) {
                System.out.println("+");
            } else {
                System.out.println(0);
            }
        }
        
    }
}
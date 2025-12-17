import java.util.Scanner;
import java.util.Stack;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> s = new Stack<>();
        // Please write your code here.
        for (int i=0; i<n; i++) {
            String com = sc.next();
            if (com.equals("push")) {
                int num = sc.nextInt();
                s.push(num);
            } else {
                if (com.equals("size")) {
                    System.out.println(s.size());
                } else if (com.equals("empty")) {
                    if (s.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                } else if (com.equals("pop")) {
                    System.out.println(s.pop());
                } else if (com.equals("top")) {
                    System.out.println(s.peek());
                }
            }
        }
    }
}
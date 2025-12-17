import java.util.Scanner;
import java.util.Stack;
public class Main {
    public static boolean isRight(String str) {
        Stack<Character> s = new Stack<>();
        int len = str.length();

        for (int i=0; i<len; i++) {
            if (str.charAt(i)=='(') {
                s.push('(');
            } else {
                if (!s.isEmpty()) {
                    s.pop();
                } else {
                    return false;
                }
            }
        }
        if (!s.isEmpty()) {
            return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        // Please write your code here.
       if (isRight(str)) {
        System.out.print("Yes");
       } else {
        System.out.print("No");
       }
        
    }
}
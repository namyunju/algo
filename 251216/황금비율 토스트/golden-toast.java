import java.util.Scanner;
import java.util.LinkedList;
import java.util.ListIterator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<Character> l = new LinkedList<>();
        
        int n = sc.nextInt();
        int m = sc.nextInt();

        String s = sc.next();

        sc.nextLine();

        for (int i=0; i<s.length(); i++) {
            l.add(s.charAt(i));
        }
        ListIterator<Character> it = l.listIterator(l.size());

        
        for (int i = 0; i < m; i++) {
            String command = sc.next();
            if (command.charAt(0) == 'L') {
                if (it.hasPrevious()) {
                    it.previous();
                }
            } else if (command.charAt(0) == 'P') {
                
                char c = sc.next().charAt(0);
                it.add(c);
            } else if (command.charAt(0) == 'R') {
                if (it.hasNext()) {
                    it.next();
                }
            } else if (command.charAt(0) == 'D') {
                if (it.hasNext()) {
                    it.next();
                    it.remove();
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : l) {
            sb.append(ch);
        }
        System.out.println(sb.toString());
        
        // Please write your code here.
    }
}
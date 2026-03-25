import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        Stack<Integer> stack = new Stack<>();
        boolean[] valid = new boolean[n];

        for (int i=0; i<n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                if (!stack.isEmpty()) {
                    valid[stack.pop()] = true;
                    valid[i] = true;
                }
            }
        }
        int maxLen = 0;
        int curLen = 0;
        for (int i=0; i<n; i++) {
            if (valid[i]) {
                curLen++;
                maxLen = Math.max(maxLen, curLen);
            } else {
                curLen = 0;
            }
        }
        System.out.println(maxLen);
    }
}
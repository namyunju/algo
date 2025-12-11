import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        // Please write your code here.
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i=0; i<n; i++) {
            String line = sc.nextLine().trim();
            String[] parts = line.split("\\s+");
            String command = parts[0];

            if (command.equals("push_back")) {
                int number = Integer.parseInt(parts[1]);
                numbers.add(number);
            } else if (command.equals("pop_back")) {
                numbers.remove(numbers.size()-1);
            } else if (command.equals("size")) {
                System.out.println(numbers.size());
            } else {
                int number = Integer.parseInt(parts[1]);
                System.out.println(numbers.get(number-1));
            }
            
        }
    }
}
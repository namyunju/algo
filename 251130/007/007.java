import java.util.Scanner;

class Agent {
    String secret;
    char place;
    int time;

    public Agent(String secret, char place, int time) {
        this.secret = secret;
        this.place = place;
        this.time = time;
    }
};

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String scode = sc.next();
        char mplace = sc.next().charAt(0);
        int time = sc.nextInt();

        Agent aagent = new Agent(scode, mplace, time);

        System.out.println("secret code : "+ aagent.secret);
        System.out.println("meeting point : " + aagent.place);
        System.out.println("time : " + aagent.time);
    }
}
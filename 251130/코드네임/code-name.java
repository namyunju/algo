import java.util.Scanner;

class Agent {
    char codename;
    int score;

    public Agent() {
        this.codename='s';
        this.score=0;
    }

    public Agent(char codename, int score) {
        this.codename = codename;
        this.score=score;
    }
};

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Please write your code here.

        Agent[] agentlist = new Agent[5];

        for (int i=0; i<5; i++) {
            char codename = sc.next().charAt(0);
            int score = sc.nextInt();

            agentlist[i] = new Agent(codename, score);
        }

        char lowAgent = agentlist[0].codename;
        int lowScore = agentlist[0].score;
        for (int i=1; i<5; i++) {
            if (lowScore > agentlist[i].score) {
                lowAgent = agentlist[i].codename;
                lowScore = agentlist[i].score;
            }
        }
        System.out.print(lowAgent + " " + lowScore);
    }
}
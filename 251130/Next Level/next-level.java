import java.util.Scanner;
class Character {
    String id;
    int level;

    public Character() {
        this.id = "codetree";
        this.level = 10;
    }

    public Character(String id, int level) {
        this.id = id;
        this.level = level;
    }
};

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id = sc.next();
        int level = sc.nextInt();
        // Please write your code here.
        Character ch1 = new Character();
        System.out.println("user " + ch1.id + " lv " + ch1.level);
        Character ch2 = new Character(id, level);
        System.out.println("user "+ ch2.id + " lv " + ch2.level);
    }
}
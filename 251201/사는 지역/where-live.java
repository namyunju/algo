import java.util.Scanner;
class Person {
    String name;
    String address;
    String loc;

    public Person(String name, String address, String loc) {
        this.name = name;
        this.address = address;
        this.loc = loc;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Person[] people = new Person[n];

        String[] names = new String[n];
        String[] addresses = new String[n];
        String[] regions = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = sc.next();
            addresses[i] = sc.next();
            regions[i] = sc.next();
            people[i] = new Person(names[i], addresses[i], regions[i]);
        }
        // Please write your code here.
        int lastIdx = 0;
        for (int i =0; i<n; i++) {
            if (people[i].name.compareTo(people[lastIdx].name) >0) {
                lastIdx = i;
            }
        }

        System.out.println("name " + people[lastIdx].name);
        System.out.println("addr " + people[lastIdx].address);
        System.out.println("city " + people[lastIdx].loc);

    }
}
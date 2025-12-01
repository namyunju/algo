import java.util.Scanner;
class Product {
    String name;
    int productCode;

    public Product(String name, int productCode) {
        this.name = name;
        this.productCode = productCode;
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id2 = sc.next();
        int code2 = sc.nextInt();
        // Please write your code here.

        Product product1 = new Product('codetree', 50);
        Product product2 = new Product(id2, code2);

        System.out.printf("product %d is %s\n", product1.name, product1.productCode);
        System.out.printf("product %d is %s\n", product2.name, product2.productCode);
    }
}
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// The main method must be in a class named "Main".
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        if (N == 1) {
            System.out.println("A");
            return;
        }
        // 숫자가 두 개가 주어진다면
        // 두 개가 동일하다면 그 다음 수도 같음
        // 다르다면 다음 수는 여러가지 가능
        if (N == 2) {
            if (arr[0] == arr[1]) {
                System.out.println(arr[0]);
                return;
            } else {
                System.out.println("A");
                return;
            }
        }

        int a = 0;
        int b = 0;

        if (arr[1]-arr[0]==0) {
            a=1;
            b=0;
        } else {
            if ((arr[2]-arr[1]) % (arr[1]-arr[0]) != 0) {
                System.out.println("B");
                return;
            }
            a = (arr[2]-arr[1]) / (arr[1]-arr[0]);
            b = arr[1] - (a * arr[0]);
        }
        for (int i=0; i<N-1; i++) {
            if (arr[i+1] != (arr[i]*a+b)) {
                System.out.println("B");
                return;
            }
        }
        System.out.println(arr[N-1]*a+b);
    
        
    }
}
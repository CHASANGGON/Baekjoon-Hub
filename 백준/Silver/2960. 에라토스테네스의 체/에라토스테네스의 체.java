import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 받기
        String input = br.readLine();

        // 공백으로 나누기
        String[] parts = input.split(" ");

        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);



        func1(n, k);

    }
    static void func1(int n, int k) {
        int[] arr = new int[n+1];
        int now = 0;

        for(int i = 2; i <= n; i++) {
            for(int j = i;j <= n; j += i) {
                if (arr[j] == 0) {
                    arr[j] = 1;
                    now += 1;
                    if (k == now) {
                        System.out.println(j);
                        return;
                    }

                }
            }
        }
    }
}
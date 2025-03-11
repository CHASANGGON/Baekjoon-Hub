import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // dp
        int[] dp = new int[N + 1];
        int[] path = new int[N + 1];
        Arrays.fill(dp, 1000000);
        dp[1] = 0;
        for (int i = 2; i <= N; i++) {
            if (dp[i - 1] + 1 < dp[i]) {
                dp[i] = dp[i - 1] + 1;
                path[i] = i-1;
            }

            if (i % 2 == 0 && dp[i / 2] + 1 < dp[i]) {
                dp[i] = dp[i / 2] + 1;
                path[i] = i / 2;
            }

            if (i % 3 == 0 && dp[i / 3] + 1 < dp[i]) {
                dp[i] = dp[i / 3] + 1;
                path[i] = i / 3;
            }
        }


        // 출력
        System.out.println(dp[N]);
        System.out.print(N + " ");
        while (N != 1) {
            System.out.print(path[N] + " ");
            N = path[N];
        }
    }
}

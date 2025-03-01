import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // 수열 입력 받기
        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // dp
        int maxSum = 0;
        int[] dp = new int[N];
        for (int now = N - 1; now >= 0; now--) {
            dp[now] = arr[now];
            for (int next = now + 1; next < N; next++) {
                if (arr[now] < arr[next]) {
                    dp[now] = Math.max(dp[now], arr[now] + dp[next]);
                }
            }
            maxSum = Math.max(maxSum, dp[now]);
        }

        // 출력
        System.out.println(maxSum);
    }
}
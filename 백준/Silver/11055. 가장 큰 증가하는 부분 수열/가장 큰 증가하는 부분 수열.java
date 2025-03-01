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
        int[] dp = new int[N];
        dp[N - 1] = arr[N - 1];
        for (int now = N - 2; now >= 0; now--) {
            int before = now + 1;
            if (arr[now] < arr[before]) {
                for (int next = before; next < N; next++) {
                    if (arr[now] < arr[next]) {
                        dp[now] = Math.max(dp[now], arr[now] + dp[next]);
                    }
                }
            } else {
                dp[now] = arr[now];
                for (int next = before; next < N; next++) {
                    if (arr[now] < arr[next]) {
                        dp[now] = Math.max(dp[now], arr[now] + dp[next]);
                    }
                }
            }
        }

        // 출력
        int maxSum = 0;
        for (int i = 0; i < N; i++) {
            maxSum = Math.max(maxSum, dp[i]);
        }
        System.out.println(maxSum);
    }
}
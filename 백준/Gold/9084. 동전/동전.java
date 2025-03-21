import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine()); // 동전 종류 개수
            int[] coins = new int[N]; // 동전 배열

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                coins[i] = Integer.parseInt(st.nextToken());
            }

            int M = Integer.parseInt(br.readLine()); // 목표 금액
            int[] dp = new int[M + 1]; // dp 테이블 (0 ~ M)
            dp[0] = 1; // 0원을 만드는 방법은 1가지 (아무것도 안 쓰는 경우)

            // 동전마다 DP 갱신
            for (int coin : coins) {
                for (int j = coin; j <= M; j++) {
                    dp[j] += dp[j - coin];
                }
            }

            System.out.println(dp[M]); // M원을 만들 수 있는 경우의 수 출력
        }
    }
}

import java.io.*;

public class Main {
    static final int MOD = 1000000; // 정답이 너무 클 수 있으니까 나머지 처리

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        // 예외 처리: 0으로 시작하면 애초에 해석 불가
        if (s.charAt(0) == '0') {
            System.out.println(0);
            return;
        }

        int n = s.length();
        int[] dp = new int[n + 1];

        dp[0] = 1; // 아무것도 해석 안 한 경우는 1가지
        dp[1] = 1; // 첫 글자가 0이 아니라면 해석 1가지 가능

        for (int i = 2; i <= n; i++) {
            // 한 자리 숫자
            int oneDigit = s.charAt(i - 1) - '0';
            if (oneDigit >= 1 && oneDigit <= 9) {
                dp[i] = (dp[i] + dp[i - 1]) % MOD;
            }

            // 두 자리 숫자
            int twoDigit = (s.charAt(i - 2) - '0') * 10 + oneDigit;
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] = (dp[i] + dp[i - 2]) % MOD;
            }
        }

        System.out.println(dp[n]);
    }
}

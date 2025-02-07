import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // M, N 입력 받기
        String[] MN = br.readLine().split(" ");
        int M = Integer.parseInt(MN[0]); // 조카의 수
        int N = Integer.parseInt(MN[1]); // 막대의 수

        // 막대 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sticks = new int[N];
        int right = 1;
        for (int i = 0; i < N; i++) {
            int stick = Integer.parseInt(st.nextToken());
            sticks[i] = stick;
            right = Math.max(stick, right);
        }

        int left = 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            int cnt = 0;
            for (int i = 0; i < N; i++) {
                cnt += sticks[i] / mid;
            }

            if (cnt >= M) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(left - 1);
    }
}
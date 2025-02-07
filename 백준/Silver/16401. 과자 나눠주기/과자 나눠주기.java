import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 입력 받기
        int M = sc.nextInt();  // 조카 수
        int N = sc.nextInt();  // 과자 개수
        int[] snacks = new int[N];
        
        int maxLen = 0;
        for (int i = 0; i < N; i++) {
            snacks[i] = sc.nextInt();
            maxLen = Math.max(maxLen, snacks[i]);  // 가장 긴 과자 길이 찾기
        }
        
        // 이진 탐색 (1 ~ maxLen)
        int left = 1, right = maxLen;
        int result = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canDistribute(snacks, M, mid)) {
                result = mid;  // 현재 길이로 나눠줄 수 있으면 정답 후보
                left = mid + 1; // 더 긴 과자 시도
            } else {
                right = mid - 1; // 더 짧은 과자 시도
            }
        }

        System.out.println(result);
    }

    // 특정 길이 mid로 과자를 나누었을 때 M명에게 줄 수 있는지 확인
    private static boolean canDistribute(int[] snacks, int M, int mid) {
        if (mid == 0) return false;  // 길이가 0이면 나눌 수 없음
        
        int count = 0;
        for (int snack : snacks) {
            count += snack / mid;  // 각 과자를 mid 길이로 나눌 때 개수
        }

        return count >= M;  // M명 이상에게 나눠줄 수 있으면 true
    }
}

import java.io.*;
import java.util.*;

class Main {
    static int N, H;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N, H 입력 받기
        N = Integer.parseInt(st.nextToken()); // 가로
        H = Integer.parseInt(st.nextToken()); // 세로

        // 배열 생성
        int[] top = new int[N / 2];
        int[] bot = new int[N / 2];
        for (int i = 0; i < N / 2; i++) {
            bot[i] = Integer.parseInt(br.readLine());
            top[i] = Integer.parseInt(br.readLine());
        }

        // 정렬
        Arrays.sort(bot); // 100,000 log (100,000) ~= 1,700,000
        Arrays.sort(top);

        // 변수 생성
        int cnt = 1;
        int minH = 2 * N;

        // 모든 높이에 대해서 검사
        for (int h = 0; h < H; h++) {
            // h가 1일 때,  bot 1은 만나지 않은 걸로

            // 이분 탐색
            int botCnt = binarySearch(bot, h); // 높이가 h 이상인 개수
            int topCnt = binarySearch(top, H - h - 1);

            int total = botCnt + topCnt;

            if (total < minH) {
                minH = total;
                cnt = 1;
            } else if (total == minH) {
                cnt++;
            }
        }

        System.out.println(minH + " " + cnt);
    }

    // target보다 큰 개수를 반환
    private static int binarySearch(int[] arr, int target) {
        int left = 0, right = N / 2 - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (target < arr[mid]) {
                right = mid - 1;
            } else if (target >= arr[mid]) {
                left = mid + 1;
            }
        }

        return N / 2 - left;
    }
}
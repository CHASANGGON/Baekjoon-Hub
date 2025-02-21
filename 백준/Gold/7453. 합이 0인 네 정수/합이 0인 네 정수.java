import java.io.*;
import java.util.*;

public class Main {
    private static int N;
    private static long[] A, B, C, D;
    private static Map<Long, Long> hashMap;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 1. 입력 받기
        N = Integer.parseInt(br.readLine());
        A = new long[N];
        B = new long[N];
        C = new long[N];
        D = new long[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
        }

        // 2. C + D 값을 해시맵에 저장
        makeHashMap();

        // 3. A + B의 합이 -(C + D)가 되는 경우 카운트
        long cnt = countZeroSums();

        // 4. 출력 최적화 (BufferedWriter 사용)
        bw.write(cnt + "\n");
        bw.flush();
        bw.close();
    }

    private static void makeHashMap() {
        hashMap = new HashMap<>(N * N);  // 해시맵 초기 크기 설정

        for (int i = 0; i < N; i++) { // C
            for (int j = 0; j < N; j++) { // D
                long sumCD = C[i] + D[j];
                hashMap.put(sumCD, hashMap.getOrDefault(sumCD, 0L) + 1L);
            }
        }
    }

    private static long countZeroSums() {
        long cnt = 0;

        for (int i = 0; i < N; i++) { // A
            for (int j = 0; j < N; j++) { // B
                long sumAB = A[i] + B[j];
                cnt += hashMap.getOrDefault(-sumAB, 0L); // **반드시 -sumAB!**
            }
        }

        return cnt;
    }
}

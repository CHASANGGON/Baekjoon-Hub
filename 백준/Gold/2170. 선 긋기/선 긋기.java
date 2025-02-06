import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastReader reader = new FastReader();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = reader.nextInt();
        int[][] xy = new int[N][2];

        // 입력 최적화
        for (int i = 0; i < N; i++) {
            xy[i][0] = reader.nextInt();
            xy[i][1] = reader.nextInt();
        }

        // 정렬 최적화 (멀티스레딩 활용)
        Arrays.parallelSort(xy, Comparator.comparingInt(a -> a[0]));

        // 선분 합치기
        int ans = 0;
        int[] before = {xy[0][0], xy[0][1]};
        for (int i = 1; i < N; i++) {
            int front = xy[i][0];
            int end = xy[i][1];

            if (before[1] < front) { // 끊기는 경우
                ans += (before[1] - before[0]); // 지금까지의 길이 누적
                before[0] = front;
                before[1] = end;
            } else { // 이어지는 경우
                before[1] = Math.max(end, before[1]);
            }
        }

        // 최종 출력 최적화
        bw.write(ans + (before[1] - before[0]) + "\n");
        bw.flush();
    }

    // 빠른 입력 클래스
    static class FastReader {
        final int SIZE = 1 << 15;
        byte[] buffer = new byte[SIZE];
        int index, size;
        InputStream in;

        FastReader() {
            in = System.in;
        }

        int nextInt() throws IOException {
            int n = 0;
            byte c;
            while ((c = read()) <= 32);
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                n = (n << 3) + (n << 1) + (c & 15);
            } while (isNumber(c = read()));
            return neg ? -n : n;
        }

        boolean isNumber(byte c) {
            return 47 < c && c < 58;
        }

        byte read() throws IOException {
            if (index == size) {
                size = in.read(buffer, index = 0, SIZE);
                if (size < 0) buffer[0] = -1;
            }
            return buffer[index++];
        }
    }
}

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String king = st.nextToken();
        String stone = st.nextToken();
        int n = Integer.parseInt(st.nextToken());

        int kingC = king.charAt(0) - 64;
        int kingR = king.charAt(1) - '0';
        int stoneC = stone.charAt(0) - 64;
        int stoneR = stone.charAt(1) - '0';

        // 방향 이동 정의
        Map<String, int[]> directions = new HashMap<>();
        directions.put("R", new int[]{1, 0});
        directions.put("L", new int[]{-1, 0});
        directions.put("B", new int[]{0, -1});
        directions.put("T", new int[]{0, 1});
        directions.put("RT", new int[]{1, 1});
        directions.put("LT", new int[]{-1, 1});
        directions.put("RB", new int[]{1, -1});
        directions.put("LB", new int[]{-1, -1});

        for (int i = 0; i < n; i++) {
            String move = br.readLine();
            int[] dir = directions.get(move);

            // 킹 이동
            int nextKingC = kingC + dir[0];
            int nextKingR = kingR + dir[1];

            // 돌과의 충돌 확인
            if (nextKingC == stoneC && nextKingR == stoneR) {
                int nextStoneC = stoneC + dir[0];
                int nextStoneR = stoneR + dir[1];

                // 돌이 체스판 안에 있어야 이동 가능
                if (nextStoneC >= 1 && nextStoneC <= 8 && nextStoneR >= 1 && nextStoneR <= 8) {
                    stoneC = nextStoneC;
                    stoneR = nextStoneR;
                    kingC = nextKingC;
                    kingR = nextKingR;
                }
            } else {
                // 킹이 체스판 안에 있어야 이동 가능
                if (nextKingC >= 1 && nextKingC <= 8 && nextKingR >= 1 && nextKingR <= 8) {
                    kingC = nextKingC;
                    kingR = nextKingR;
                }
            }
        }

        // 결과 출력
        System.out.println(String.format("%c%d", kingC + 64, kingR));
        System.out.println(String.format("%c%d", stoneC + 64, stoneR));
    }
}

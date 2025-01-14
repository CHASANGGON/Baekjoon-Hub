import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());
        String[] numsN = br.readLine().split(" ");

        Map<Integer, Integer> mapA = new HashMap<>();
        for (int i = 0; i < N; i++) {
            findDivisor(Integer.parseInt(numsN[i]), mapA);
        }

        // M 입력 받기
        int M = Integer.parseInt(br.readLine());
        String[] numsM = br.readLine().split(" ");

        Map<Integer, Integer> mapB = new HashMap<>();
        for (int i = 0; i < M; i++) {
            findDivisor(Integer.parseInt(numsM[i]), mapB);
        }

        long gcd = 1;
        boolean flag = false;
        for (int divisorA : mapA.keySet()) {
            if (mapB.containsKey(divisorA)) {
                int minCount = Math.min(mapA.get(divisorA), mapB.get(divisorA));
                for (int i = 0; i < minCount; i++) {
                    gcd *= divisorA;
                    if (gcd >= 1_000_000_000) { 
                        flag = true;
                        gcd %= 1_000_000_000;
                    }
                }
            }
        }

        // ✅ flag가 true면 항상 9자리로 고정 출력
        if (flag) {
            System.out.printf("%09d\n", gcd);
        } else {
            System.out.println(gcd);
        }
    }

    private static void findDivisor(int num, Map<Integer, Integer> map) {
        for (int i = 2; i * i <= num; i++) {
            while (num % i == 0) {
                map.put(i, map.getOrDefault(i, 0) + 1);
                num /= i;
            }
        }

        if (num > 1) { // ✅ num이 소수인 경우 처리
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
    }
}

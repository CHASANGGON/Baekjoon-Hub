import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력
        int N = Integer.parseInt(br.readLine());

        // 수 입력
        Map<Character, Long> weightMap = new HashMap<>(); // 가중치를 저장할 맵
        Set<Character> firstChars = new HashSet<>(); // 맨 앞자리에 오는 문자를 저장할 셋

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            firstChars.add(input.charAt(0)); // 제일 앞 문자 기록

            int numLength = input.length();

            for (int j = 0; j < numLength; j++) {
                Character ch = input.charAt(j); // 현재 문자
                Long weight = (long) Math.pow(10, numLength - 1 - j); // 자리수를 고려한 가중치

                weightMap.put(ch, weightMap.getOrDefault(ch, 0L) + weight); // 맵에 가중치 누적합 저장
            }
        }

        // greedy - 가중치 내림차순으로 정렬
        List<Character> chars = new ArrayList<>(weightMap.keySet());
        chars.sort((a, b) -> Long.compare(weightMap.get(b), weightMap.get(a)));

        // 핵심 로직: 10개 알파벳이 모두 사용되고, 가중치 최대인 것이 첫 번째 문자인 경우
        if (chars.size() == 10 && firstChars.contains(chars.get(0))) {
            // 첫 번째 문자가 아닌 것들 중에서 가중치가 가장 작은 것 찾기
            Character zeroCandidate = null;
            for (int i = chars.size() - 1; i >= 0; i--) {
                if (!firstChars.contains(chars.get(i))) {
                    zeroCandidate = chars.get(i);
                    break;
                }
            }
            
            // 0으로 할당할 문자를 맨 뒤로 이동
            if (zeroCandidate != null) {
                chars.remove(zeroCandidate);
                chars.add(zeroCandidate);
            }
        }

        // 9부터 차례로 할당하여 합 계산
        long ans = 0;
        int digit = 9;
        for (Character ch : chars) {
            ans += digit-- * weightMap.get(ch);
        }

        // 출력
        System.out.println(ans);
    }
}
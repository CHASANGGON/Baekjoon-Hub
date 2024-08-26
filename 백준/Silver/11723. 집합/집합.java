import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();
        int S = 0;  // 집합을 비트마스크로 표현한 변수
        int operationCount = Integer.parseInt(reader.readLine());  // 연산의 수를 입력받음

        while (operationCount-- > 0) {  // operationCount 만큼 반복
            String[] input = reader.readLine().split(" ");
            String command = input[0];  // 명령어를 읽음

            if (command.equals("all"))
                S = (1 << 21) - 1;  // S를 {1, 2, ..., 20}으로 설정
            else if (command.equals("empty"))
                S = 0;  // S를 공집합으로 설정
            else {
                int x = Integer.parseInt(input[1]);  // x값을 읽음
                if (command.equals("add"))
                    S |= (1 << x);  // x를 집합에 추가
                else if (command.equals("remove"))
                    S &= ~(1 << x);  // x를 집합에서 제거
                else if (command.equals("check"))
                    output.append((S & (1 << x)) != 0 ? 1 : 0).append("\n");  // x가 집합에 있는지 확인
                else if (command.equals("toggle"))
                    S ^= (1 << x);  // x가 있으면 제거, 없으면 추가
            }
        }
        System.out.println(output);  // 결과 출력
    }
}

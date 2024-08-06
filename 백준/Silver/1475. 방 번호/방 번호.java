import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 입력을 받기 위한 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력받은 문자열을 읽음
        String ss = br.readLine();

        // 0부터 9까지의 숫자의 빈도를 저장하기 위한 배열 생성
        int[] arr = new int[10];

        // 문자열의 각 문자에 대해 반복
        for (int i = 0; i < ss.length(); i++) {
            // 현재 문자를 추출
            char c = ss.charAt(i);

            // 현재 문자가 숫자 '0'에서 '9' 사이인지 확인
            if (c >= '0' && c <= '9') {
                // 문자 '0'의 ASCII 값을 48로 빼서 숫자로 변환
                //  '0' - '0' = 0(int)
                int index = c - '0';
                // 해당 숫자의 빈도를 1 증가
                arr[index]++;
            }
        }

        // 배열의 내용을 문자열로 변환하여 출력
        // Arrays.toString()을 사용하면 배열의 내용을 보기 쉽게 출력할 수 있음
        // System.out.println(Arrays.toString(arr)); // 123412 -> [0, 2, 2, 1, 1, 0, 0, 0, 0, 0]

        arr[6] = (int) Math.round(((double) arr[6] + (double) arr[9]) / 2);
        int max = 0;
        for (int i = 0; i < 9; i++) {
            if (arr[i] > max)
                max = arr[i];
        }

        System.out.println(max);
    }
}

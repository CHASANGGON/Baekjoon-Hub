import java.io.*;

class Main {
    static int count; // recursion 호출 횟수 세는 변수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            String s = br.readLine();
            count = 0; // 매 테스트케이스마다 초기화
            int result = isPalindroms(s);
            System.out.println(result + " " + count);
        }
    }

    private static int recursion(String s, int l, int r) {
        count++; // recursion 호출될 때마다 + 1
        if (l >= r) return 1;
        else if (s.charAt(l) != s.charAt(r)) return 0; // 양 끝에서부터 문자 비교
        else return recursion(s, l + 1, r - 1);
    }

    private static int isPalindroms(String s) {
        return recursion(s, 0, s.length() - 1);
    }
}
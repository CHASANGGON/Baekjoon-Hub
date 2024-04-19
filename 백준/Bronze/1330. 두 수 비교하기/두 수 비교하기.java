import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력을 받기 위한 객체 생성
        
        String str = br.readLine(); // 한 줄 입력 받기
        StringTokenizer st = new StringTokenizer(str," "); // 공백을 기준으로 나누기 위한 객체 생성
        
        int A = Integer.parseInt(st.nextToken()); // 토큰을 하나씩 넘겨주면서 정수로 변환
        int B = Integer.parseInt(st.nextToken());

        if(A > B) System.out.println(">");
        else if(A < B) System.out.println("<");
        else System.out.println("==");
    }    
}
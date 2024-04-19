import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Set<String> set = new HashSet<>();
        set.add("ChongChong"); // 총총이는 어차피 추가해야함

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String person1 = st.nextToken();
            String person2 = st.nextToken();
            if (set.contains(person1) || set.contains(person2)) { // 둘 중 한 명이라도 해쉬셋에 있으면
                set.add(person1); // 둘 다 추가
                set.add(person2); // 둘 다 추가
            }
        }
        System.out.println(set.size());
    }
}
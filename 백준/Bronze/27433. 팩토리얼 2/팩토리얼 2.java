import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println(factorial(N));
    }

    private static long factorial(int N) {
        if (N == 1 || N == 0) {
            return 1;
        }
        return N * factorial(N - 1);
    }
}
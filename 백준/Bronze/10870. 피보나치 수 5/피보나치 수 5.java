import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        // 피보나치 수열의 첫 두 항은 특별 처리
        if (n == 0) {
            System.out.println(0);
            return;
        } else if (n == 1) {
            System.out.println(1);
            return;
        }

        int before = 0;
        int next = 1;
        int temp;

        for (int i = 2; i <= n; i++) {
            temp = next;
            next += before;
            before = temp;
        }

        System.out.println(next);
    }
}
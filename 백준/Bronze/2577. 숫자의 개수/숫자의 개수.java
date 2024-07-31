import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int res = scanner.nextInt() * scanner.nextInt() * scanner.nextInt();

        int[] res_Arr = new int[10];
        while(res > 0){
            res_Arr[res % 10]++;
            res /= 10;
        }

        for (int i = 0; i< 10;i++) {
            System.out.println(res_Arr[i]);
        }
    }
}
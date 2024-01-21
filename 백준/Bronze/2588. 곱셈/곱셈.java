import java.util.Scanner;
    
public class Main{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt(); int B = sc.nextInt();
        int B_1 = (B % 100) % 10; 
        int B_10 = (B % 100) / 10; 
        int B_100 = B / 100;    
        System.out.println(A * B_1);
        System.out.println(A * B_10);
        System.out.println(A * B_100);
        System.out.println(A * (B_100 * 100 + B_10 * 10 + B_1 * 1));
    }   
}
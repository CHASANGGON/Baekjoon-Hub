import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for(char b : a.toCharArray()) {
            if(Character.isUpperCase(b)) {
                System.out.print(Character.toLowerCase(b));
            } else {
                System.out.print(Character.toUpperCase(b));
            }
        }
    }
} 
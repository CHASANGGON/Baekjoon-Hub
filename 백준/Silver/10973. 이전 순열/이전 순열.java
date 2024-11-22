import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numArr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numArr[i] = Integer.parseInt(st.nextToken());
        }

        if (prevPermutation(numArr)) {
            for (int i = 0; i < n; i++) {
                System.out.print(numArr[i] + (i < n - 1 ? " " : ""));
            }
        } else {
            System.out.println(-1);
        }
    }

    public static boolean prevPermutation(int[] numArr) {
        int n = numArr.length;

        // Step 1: Find the largest i such that numArr[i] > numArr[i+1]
        int i = n - 2;
        while (i >= 0 && numArr[i] <= numArr[i + 1]) {
            i--;
        }

        // If no such i exists, the array is already the smallest permutation
        if (i < 0) return false;

        // Step 2: Find the largest j such that numArr[j] < numArr[i]
        int j = n - 1;
        while (numArr[j] >= numArr[i]) {
            j--;
        }

        // Step 3: Swap numArr[i] and numArr[j]
        swap(numArr, i, j);

        // Step 4: Reverse the order of elements from i+1 to the end
        reverse(numArr, i + 1, n - 1);

        return true;
    }

    public static void swap(int[] numArr, int i, int j) {
        int temp = numArr[i];
        numArr[i] = numArr[j];
        numArr[j] = temp;
    }

    public static void reverse(int[] numArr, int start, int end) {
        while (start < end) {
            swap(numArr, start++, end--);
        }
    }
}

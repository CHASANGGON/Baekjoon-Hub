import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] HW = br.readLine().split(" ");
        int H = Integer.parseInt(HW[0]);
        int W = Integer.parseInt(HW[1]);

        String[] heightsString = br.readLine().split(" ");
        int[] heights = new int[W];

        int maxIndex = 0;
        int maxHeight = 0;
        for (int i = 0; i < W; i++) {
            heights[i] = Integer.parseInt(heightsString[i]);
            if (maxHeight < heights[i]) {
                maxHeight = heights[i];
                maxIndex = i;
            }
        }


        int water = 0;
        int left = 0, right = 1;
        // 왼쪽 -> 최대 높이
        while (left < maxIndex) {
            while (heights[left] > heights[right] && right < maxIndex) {
                right++;
            }
            int waterHeight = Math.min(heights[left], heights[right]);
            for (int i = left + 1; i < right; i++) {
                water += waterHeight - heights[i];
            }
            left = right;
            right++;
        }

        left = W - 2;
        right = W - 1;
        // 오른쪽 -> 최대 높이
        while (left > maxIndex) {
            while (heights[left] < heights[right] && left > maxIndex) {
                left--;
            }
            int waterHeight = Math.min(heights[left], heights[right]);
            for (int i = right - 1; i > left; i--) {
                water += waterHeight - heights[i];
            }
            right = left;
            left--;
        }

        System.out.println(water);
    }
}
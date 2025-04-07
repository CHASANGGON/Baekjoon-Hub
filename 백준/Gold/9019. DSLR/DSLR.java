import java.io.*;
import java.util.*;


public class Main {
    static int A, B, numCopy, numS, numD, numL, numR;

    static class Node {
        int num;
        String commands;

        Node(int num, String commands) {
            this.num = num;
            this.commands = commands;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // T 입력받기
        int T = Integer.parseInt(br.readLine());

        // 테스트 케이스
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            // BFS
            bfs();
        }

    }

    //** BFS를 통해서 B를 찾아가는 최소 횟수를 출력하고 종료하는 함수 **/
    private static void bfs() {
        boolean[] visited = new boolean[10000]; // 방문 체크 추가
        Queue<Node> queue = new LinkedList<>();

        queue.offer(new Node(A, ""));
        visited[A] = true;

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            int num = node.num;
            String dslr = node.commands;

            // 종료 조건
            if (num == B) {
                System.out.println(dslr);
                return;
            }


            // D: *2 (+ % 10000)
            numD = num * 2;
            if (numD > 9999) numD %= 10000;
            if (!visited[numD]) {
                visited[numD] = true;
                queue.offer(new Node(numD, dslr + "D"));
            }
            // S: -1 (0 -> 9999)
            numS = num - 1;
            if (numS == -1) numS = 9999;
            if (!visited[numS]) {
                visited[numS] = true;
                queue.offer(new Node(numS, dslr + "S"));
            }

            // L: ←
            numCopy = num;
            int num1 = (int) numCopy / 1000;
            numCopy %= 1000;
            int num2 = (int) numCopy / 100;
            numCopy %= 100;
            int num3 = (int) numCopy / 10;
            numCopy %= 10;
            int num4 = numCopy;

            numL = 1000 * num2 + 100 * num3 + 10 * num4 + num1;
            if (!visited[numL]) {
                visited[numL] = true;
                queue.offer(new Node(numL, dslr + "L"));
            }

            // R: →
            numCopy = num;
            num1 = (int) numCopy / 1000;
            numCopy %= 1000;
            num2 = (int) numCopy / 100;
            numCopy %= 100;
            num3 = (int) numCopy / 10;
            numCopy %= 10;
            num4 = numCopy;

            numR = 1000 * num4 + 100 * num1 + 10 * num2 + num3;

            if (!visited[numR]) {
                visited[numR] = true;
                queue.offer(new Node(numR, dslr + "R"));
            }
        }

    }
}

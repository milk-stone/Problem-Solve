import java.io.*;
import java.util.Arrays;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int[] answer;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        String[] input = br.readLine().split(" ");
        int[] nm = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
        int n = nm[0];
        int m = nm[1];
        visited = new boolean[n+1];
        answer = new int[m];
        backtracking(n, m, 0, 0);
        bw.flush();
        bw.close();
    }

    public static void backtracking(int n, int m, int selected, int prev) throws IOException{
        if (selected == m) {
            for (int a : answer){
                bw.write(a + " ");
            }
            bw.write("\n");
            return;
        }
        for (int i = 1; i <= n; i++){
            if (!visited[i] && i > prev){
                answer[selected] = i;
                visited[i] = true;
                backtracking(n, m, selected + 1, i);
                answer[selected] = 0;
                visited[i] = false;
            }
        }
    }
}

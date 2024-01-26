import java.io.*;
import java.util.Arrays;

public class Main {
    static BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, m;
    static int[] answer;
    static boolean[] visited; // 기본값 false

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bf.readLine().split(" ");
        int[] temp = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
        n = temp[0];
        m = temp[1];
        answer = new int[m];
        visited = new boolean[n+1];

        backtracking(n, m, 0);
        bufferedWriter.flush();
        bufferedWriter.close();
    }

    static void backtracking(int n, int m, int selected) throws IOException{
        if (selected == m){
            for (int a : answer){
                bufferedWriter.write(a + " ");
            }
            bufferedWriter.write("\n");
            return;
        }
        for (int i = 1; i <= n; i++){
            if (!visited[i]){
                answer[selected] = i;
                visited[i] = true;
                backtracking(n, m, selected + 1);
                answer[selected] = 0;
                visited[i] = false;
            }
        }
    }
}
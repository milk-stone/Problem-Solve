import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] arr;
    static int[] result;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        result = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        solve(0);
        System.out.println(sb.toString());
    }

    static void solve(int depth) {
        if (depth == M) {
            for (int res : result) {
                sb.append(res).append(" ");
            }
            sb.append('\n');
            return;
        }
        int before = -1;
        for (int i = 0; i < N; i++) {
            if (depth <= 0) {
                if (before != arr[i]) {
                    before = arr[i];
                    result[depth] = arr[i];
                    solve(depth + 1);
                }
            } else {
                if (before != arr[i] && result[depth - 1] <= arr[i]) {
                    before = arr[i];
                    result[depth] = arr[i];
                    solve(depth + 1);
                }
            }
        }
    }
}

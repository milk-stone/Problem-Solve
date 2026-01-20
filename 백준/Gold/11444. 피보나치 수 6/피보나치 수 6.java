import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static long N;
    static HashMap<Long, Long> dp;
    static int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Long.parseLong(br.readLine());

        dp = new HashMap<>();
        dp.put(0L, 0L);
        dp.put(1L, 1L);
        
        long result = fibonacci(N);
        System.out.println(result);
    }

    public static long fibonacci(long n) {
        if (dp.containsKey(n)) {
            return dp.get(n);
        }
        long f_n, f_n1;
        if (n % 2 == 1) {
            f_n = fibonacci(n / 2);
            f_n1 = fibonacci(n / 2 + 1);
            dp.put(n, (f_n * f_n + f_n1 * f_n1) % MOD);
        } else {
            f_n = fibonacci(n / 2);
            f_n1 = fibonacci(n / 2 - 1);
            dp.put(n, (f_n * (2 * f_n1 + f_n)) % MOD);
        }
        return dp.get(n);
    }
}

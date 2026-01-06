import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());
        long phi = N;

        for (int i = 2; (long) i * i <= N; i++) {
            if (N % i == 0) {
                while (N % i == 0) {
                    N /= i;
                }
                phi /= i;
                phi *= (i - 1);
            }
        }

        if (N > 1) {
            phi /= N;
            phi *= (N - 1);
        }
        System.out.println(phi);
    }
}

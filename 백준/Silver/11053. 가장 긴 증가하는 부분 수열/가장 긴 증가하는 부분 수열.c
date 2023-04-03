#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int a[1001] = { 0, }, b[1001] = { 0, }, dp[1001] = { 0, };

int main(void) {
	int N, c, max = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", a + i);
	}
	for (int k = 1; k <= N; k++) {
		c = 0;
		for (int i = 0; i < k; i++) {
			if (a[i] < a[k]) {
				b[c] = dp[i] + 1;
				c++;
			}
		}
		for (int j = 0; j < c; j++) {
			if (max < b[j]) {
				max = b[j];
			}
		}
		dp[k] = max;
		int b[1001] = { 0, };
		max = 0;
	}
	max = 0;
	for (int k = 1; k <= N; k++) {
		if (max < dp[k]) {
			max = dp[k];
		}
	}
	printf("%d", max);
	return 0;
}
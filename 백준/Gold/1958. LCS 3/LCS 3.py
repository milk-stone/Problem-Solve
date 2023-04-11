import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
dp = [[[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)] for _ in range(len(c) + 1)]
for i in range(1, len(c) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(a) + 1):
            if c[i-1] == b[j-1] and b[j-1] == a[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            elif c[i-1] == b[j-1] and c[i-1] != a[k-1]:
                dp[i][j][k] = max(dp[i-1][j-1][k], dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            elif c[i-1] == a[k-1] and c[i-1] != b[j-1]:
                dp[i][j][k] = max(dp[i-1][j][k-1], dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            elif b[j-1] == a[k-1] and c[i-1] != b[j-1]:
                dp[i][j][k] = max(dp[i][j-1][k-1], dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[-1][-1][-1])
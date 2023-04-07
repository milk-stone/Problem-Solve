import sys

input = sys.stdin.readline

n = int(input())
dp = [987654321 for _ in range(n+1)]
if n >= 2:
    dp[2] = 1
if n >= 4:
    dp[4] = 2
if n >= 5:
    dp[5] = 1
for i in range(6, n+1):
    if dp[i-2] == 987654321 and dp[i-5] != 987654321:
        dp[i] = dp[i-5] + 1
    elif dp[i-2] != 987654321 and dp[i-5] == 987654321:
        dp[i] = dp[i-2] + 1
    elif dp[i-2] != 987654321 and dp[i-5] != 987654321:
        dp[i] = min(dp[i-2], dp[i-5]) + 1
    else:
        continue
if dp[n] == 987654321:
    print(-1)
else:
    print(dp[n])

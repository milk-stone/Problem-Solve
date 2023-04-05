import sys

input = sys.stdin.readline

s1 = '0' + input().strip()
s2 = '0' + input().strip()

dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
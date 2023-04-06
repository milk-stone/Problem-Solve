import sys

input = sys.stdin.readline

t, w = map(int, input().split())
arr = [0]
for _ in range(t):
    arr.append(int(input()))
dp = [[0 for _ in range(t+1)] for _ in range(w+1)]
# 0일 때 1시작 1일때 2시작
for i in range(w+1):
    for j in range(i, t+1):
        if i%2:
            if arr[j] == 2:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1])
        else:
            if arr[j] == 1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1])
maxValue = 0
for i in dp:
    if maxValue < max(i):
        maxValue = max(i)
print(maxValue)

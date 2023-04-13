import sys

input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
skip = [[False for _ in range(n)] for _ in range(n)]
dp = [i+1 for i in range(n)]


for start in range(n-1):
    sign = 1
    temp = 0
    for i in range(start, n):
        temp += stones[i] * sign
        sign *= -1
        if temp == 0:
            skip[start][i] = True

for i in range(n-1):
    for j in range(i+1, n):
        if skip[i][j]:
            if i == 0:
                dp[j] = min(j-i, dp[j])
            else:
                dp[j] = min(j-i+dp[i-1], dp[j])
print(dp[-1])

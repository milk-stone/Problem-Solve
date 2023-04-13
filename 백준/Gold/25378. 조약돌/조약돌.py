import sys

input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
skip = [[False for _ in range(n+1)] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
dp[1] = 1


for start in range(1, n):
    sign = 1
    temp = 0
    for i in range(start, n+1):
        temp += stones[i-1] * sign
        sign *= -1
        if temp == 0:
            skip[start][i] = True


for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    for j in range(1, i):
        if skip[j][i]:
            dp[i] = min(i - j + dp[j-1], dp[i])
print(dp[-1])

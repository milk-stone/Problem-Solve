import sys

input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
skip = [[False for _ in range(n)] for _ in range(n)]
dp = [[987654321 for _ in range(n)] for _ in range(n)]


def solve(start, end):
    if start == end:
        dp[start][end] = 1
        return dp[start][end]
    if dp[start][end] != 987654321:
        return dp[start][end]
    if skip[start][end]:
        dp[start][end] = end - start
    for i in range(start, end):
        left = solve(start, i)
        right = solve(i+1, end)
        dp[start][end] = min(left + right, dp[start][end])
    return dp[start][end]


for start in range(n-1):
    sign = 1
    temp = 0
    for i in range(start, n):
        temp += stones[i] * sign
        sign *= -1
        if temp == 0:
            skip[start][i] = True

print(solve(0, n-1))

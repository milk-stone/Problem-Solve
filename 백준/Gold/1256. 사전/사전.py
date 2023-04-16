import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
dp = [[1 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
ans = ''

def solve(n, m, start, end):
    global ans
    if len(ans) == N + M:
        print(ans)
        return
    if n == 0:
        temp = len(ans)
        for i in range(N+M-temp):
            ans += 'z'
        print(ans)
        return
    if m == 0:
        temp = len(ans)
        for i in range(N+M-temp):
            ans += 'a'
        print(ans)
        return
    if K < start + dp[n-1][m]:
        ans += 'a'
        solve(n-1, m, start, start + dp[n-1][m])
    else:
        ans += 'z'
        solve(n, m-1, start + dp[n-1][m], end)


if K > dp[N][M]:
    print(-1)
else:
    solve(N, M, 1, K+1)

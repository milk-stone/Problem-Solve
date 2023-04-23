import sys

input = sys.stdin.readline

def dfs(sy, sx):
	if sy == n-1 and sx == m-1:
		return 1
	if dp[sy][sx] != -1:
		return dp[sy][sx]
	ways = 0
	for i in range(4):
		ny, nx = sy + dy[i], sx + dx[i]
		if 0 <= ny < n and 0 <= nx < m and board[sy][sx] > board[ny][nx]:
			ways += dfs(ny, nx)
	dp[sy][sx] = ways
	return dp[sy][sx]

n, m = map(int, input().split())
board = []
dp = [[-1 for _ in range(m)] for _ in range(n)]
for _ in range(n):
	board.append(list(map(int, input().split())))
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
print(dfs(0, 0))
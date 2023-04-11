import sys

input = sys.stdin.readline

n = int(input())
m = []
for i in range(n):
	m.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n): # i: 탐색할 행렬 개수
	for j in range(n-i):
		if i==1:
			dp[j][j+i] = m[j][0]*m[j][1]*m[j+1][1]
			continue
		dp[j][j+i] = 2**32
		for k in range(j, j+i):
			dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + m[j][0]*m[k][1]*m[j+i][1])
print(dp[0][n-1])
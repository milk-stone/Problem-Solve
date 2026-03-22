import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
result = []

def dfs(y, x, index):
	board[y][x] = 0
	result[index] += 1
	for i in range(4):
		ny, nx = y + dy[i], x + dx[i]
		if 0<=ny<n and 0<=nx<n and board[ny][nx] == 1:
			dfs(ny, nx, index)

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
index = -1	
for i in range(n):
	for j in range(n):
		if board[i][j] == 1:
			result.append(0)
			index += 1
			dfs(i, j, index)
print(len(result))
result.sort()
for i in result:
	print(i)
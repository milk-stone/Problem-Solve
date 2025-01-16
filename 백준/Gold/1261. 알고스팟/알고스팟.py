import sys
from collections import deque

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


M, N = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque([(0, 0)])
visited[0][0] = 0

while q:
    y, x = q.popleft()
    if y == N-1 and x == M-1:
        break
    for dy, dx in dydx:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if visited[ny][nx] == -1:
            if board[ny][nx] == 0:
                visited[ny][nx] = visited[y][x]
                q.appendleft((ny, nx))
            elif board[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

print(visited[N-1][M-1])
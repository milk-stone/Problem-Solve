import sys
from collections import deque

input = sys.stdin.readline

def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    safedis = 987654321
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                safedis = min(safedis, visited[i][j])
    return safedis


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dydx = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

ans = 0
for y in range(n):
    for x in range(m):
        if a[y][x] != 1:
            ans = max(ans, bfs(y, x))
print(ans)

from collections import deque
import sys

input = sys.stdin.readline

dydx = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

T = int(input())
for _ in range(T):
    I = int(input())
    board = [[False for _ in range(I)] for _ in range(I)]
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    q = deque([(sy, sx, 0)])
    board[sy][sx] = True
    while q:
        y, x, count = q.popleft()
        if y == ey and x == ex:
            print(count)
            break
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < I and 0 <= nx < I and not board[ny][nx]:
                q.append((ny, nx, count + 1))
                board[ny][nx] = True

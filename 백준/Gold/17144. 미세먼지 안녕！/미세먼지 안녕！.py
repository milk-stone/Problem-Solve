import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(R)]

dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

t = 1

up = [-1, -1]
down = [-1, -1]
for i in range(R - 2):
    if b[i][0] == -1:
        up = [i, 0]
        down = [i + 1, 0]
        break

while t <= T:

    # Phase 1 - 미세먼지 확산
    q = deque()
    for y in range(R):
        for x in range(C):
            if b[y][x] != 0 and b[y][x] != -1:
                q.append((y, x, b[y][x]))

    while q:
        y, x, v = q.popleft()
        nextV = v // 5
        count = 0
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if b[ny][nx] == -1:
                continue
            b[ny][nx] += nextV
            count += 1
        b[y][x] -= count * nextV


    # Phase 2 - 공기청정기 작동

    ## Phase 2.1 - up 작동
    y, x = up[0] - 1, up[1]
    for ny in range(y, 0, -1):
        b[ny][x] = b[ny - 1][x]
    y, x = 0, 0
    for nx in range(0, C - 1):
        b[y][nx] = b[y][nx + 1]
    y, x = 0, C - 1
    for ny in range(0, up[0]):
        b[ny][x] = b[ny + 1][x]
    y, x = up[0], C - 1
    for nx in range(x, 1, -1):
        b[y][nx] = b[y][nx - 1]
    b[y][1] = 0

    ## Phase 2.2 - down 작동
    y, x = down[0] + 1, down[1]
    for ny in range(y, R - 1):
        b[ny][x] = b[ny + 1][x]
    y, x = R - 1, 0
    for nx in range(0, C - 1):
        b[y][nx] = b[y][nx + 1]
    y, x = R - 1, C - 1
    for ny in range(y, down[0], -1):
        b[ny][x] = b[ny - 1][x]
    y, x = down[0], C - 1
    for nx in range(x, 1, -1):
        b[y][nx] = b[y][nx - 1]
    b[y][1] = 0

    t += 1

# calculate ANS
ans = 0
for y in range(R):
    for x in range(C):
        if b[y][x] != -1:
            ans += b[y][x]
print(ans)
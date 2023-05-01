import sys
from collections import deque

input = sys.stdin.readline

def inRange(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True
    else:
        return False

def nextFish(sy, sx, size):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque([(sy, sx, 0)])
    visited[sy][sx] = True
    Y, X, DISTANCE = -1, -1, 987654321
    while queue:
        y, x, distance = queue.popleft()
        if distance > DISTANCE:
            break
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if inRange(ny, nx) and not visited[ny][nx] and size >= board[ny][nx]:
                if board[ny][nx] != 0 and size != board[ny][nx]:
                    if distance + 1 < DISTANCE:
                        Y = ny
                        X = nx
                        DISTANCE = distance + 1
                    elif distance + 1 == DISTANCE:
                        if ny < Y:
                            Y = ny
                            X = nx
                            DISTANCE = distance + 1
                        elif ny == Y:
                            if nx < X:
                                Y = ny
                                X = nx
                                DISTANCE = distance + 1
                else:
                    queue.append((ny, nx, distance + 1))
                    visited[ny][nx] = True
    return Y, X, DISTANCE
                

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

sy, sx = -1, -1
flag = False
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sy, sx = i, j
            board[i][j] = 0
            flag = True
            break
    if flag:
        break

dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
time = 0
size = 2
ate = 0
q = deque([(sy, sx)])
while q:
    y, x = q.popleft()
    ny, nx, distance = nextFish(y, x, size)
    if ny == -1 and nx == -1:
        break
    board[ny][nx] = 0
    q.append((ny, nx))
    ate += 1
    if ate == size:
        size += 1
        ate = 0
    time += distance
print(time)

import sys
import copy

input = sys.stdin.readline

def solve(sy, sx, board, total):
    global ans
    ans = max(ans, total)
    #물고기 이동
    for i in range(1, 17):
        fy, fx = -1, -1
        for n in range(4):
            for m in range(0, 8, 2):
                if board[n][m] == i:
                    fy, fx = n, m
                    break
            if fy != -1 and fx != -1:
                break
        ##############################
        if fy == -1 and fx == -1:
            continue
        ##############################
        for c in range(8):
            dy, dx = dydx[board[n][m+1]]
            ny, nx = fy + dy, fx + dx
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 8:
                board[fy][fx+1] = (board[fy][fx+1] + 1)%8
                continue
            elif ny == sy and nx == sx:
                board[fy][fx+1] = (board[fy][fx+1] + 1)%8
                continue
            board[fy][fx], board[ny][nx] = board[ny][nx], board[fy][fx]
            board[fy][fx+1], board[ny][nx+1] = board[ny][nx+1], board[fy][fx+1]
            break
    #상어 이동
    dy, dx = dydx[board[sy][sx+1]]
    ny, nx = sy + dy, sx + dx
    while 0 <= ny < 4 and 0 <= nx < 8:
        if board[ny][nx] == 0:
            ny += dy
            nx += dx
            continue
        temp = board[ny][nx]
        board[ny][nx] = 0
        solve(ny, nx, copy.deepcopy(board), total + temp)
        board[ny][nx] = temp
        ny += dy
        nx += dx


dydx = [(-1, 0), (-1, -2), (0, -2), (1, -2), (1, 0), (1, 2), (0, 2), (-1, 2)]
a = [list(map(int, input().split())) for _ in range(4)]
for i in range(4):
    for j in range(1, 8, 2):
        a[i][j] -= 1

ans = 0
first = a[0][0]
a[0][0] = 0
solve(0, 0, copy.deepcopy(a), first)
print(ans)

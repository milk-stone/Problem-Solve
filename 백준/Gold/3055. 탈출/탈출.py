from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# water = [[False for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

dest_y, dest_x = -1, -1
wq = []
move = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'D':
            dest_y, dest_x = i, j
            visited[i][j] = True
        elif board[i][j] == 'S':
            move.append((i, j))
            visited[i][j] = True
        elif board[i][j] == '*':
            wq.append((i, j))
            visited[i][j] = True
        elif board[i][j] == 'X':
            visited[i][j] = True
            # water[i][j] = True
        else: continue

minute = 0
dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

finished = 0
while finished == 0:
    minute += 1
    next_wq, next_move = [], []

    for i in range(len(wq)):
        y, x = wq[i]
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                visited[ny][nx] = True
                next_wq.append((ny, nx))

    lm = len(move)
    if lm == 0: finished = 1
    for i in range(len(move)):
        y, x = move[i]
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if ny == dest_y and nx == dest_x:
                    finished = 2
                    break
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    next_move.append((ny, nx))
        if finished: break

    # print(f"\nDEBUG\n")
    # print(f"wq : {wq}, {next_wq}")
    # print(f"move : {move}, {next_move}")
    # for _ in visited:
    #     print(_)

    wq, move = next_wq, next_move

if finished == 1:
    print("KAKTUS")
elif finished == 2:
    print(minute)
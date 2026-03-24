import sys
import copy

input = sys.stdin.readline

ccty_type = {}

ccty_type[1] = [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]]
ccty_type[2] = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
ccty_type[3] = [
    [(0, 1), (1, 0)],
    [(1, 0), (0, -1)],
    [(0, -1), (-1, 0)],
    [(-1, 0), (0, 1)]
]
ccty_type[4] = [
    [(0, 1), (1, 0), (0, -1)],
    [(1, 0), (0, -1), (-1, 0)],
    [(0, -1), (-1, 0), (0, 1)],
    [(-1, 0), (0, 1), (1, 0)]
]
ccty_type[5] = [[(0, 1), (1, 0), (0, -1), (-1, 0)]]

N, M = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]

ccty = []

for i in range(N):
    for j in range(M):
        if b[i][j] != 0 and b[i][j] != 6:
            ccty.append((i, j))

ans = N * M


def solve(ccty, ccty_count, cctyIndex, board):
    global ans
    if ccty_count == cctyIndex:
        cur_ans = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cur_ans += 1
        ans = min(ans, cur_ans)
        return

    y, x = ccty[cctyIndex]
    curType = b[y][x]
    directions = ccty_type[curType]

    for direction_set in directions:
        new_board = copy.deepcopy(board)
        for dy, dx in direction_set:
            ny, nx = y, x
            while True:
                ny += dy
                nx += dx
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    break
                if board[ny][nx] == 6:
                    break
                elif 1 <= board[ny][nx] <= 5:
                    continue
                elif board[ny][nx] == 0:
                    new_board[ny][nx] = -1
                else:
                    continue
        solve(ccty, ccty_count, cctyIndex + 1, new_board)

solve(ccty, len(ccty), 0, b)
print(ans)
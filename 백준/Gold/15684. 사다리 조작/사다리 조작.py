import sys

input = sys.stdin.readline

def simulation(sp, board):
    n = sp
    for h in range(H):
        if n == 0:
            if board[h][n]:
                n += 1
        elif 0 < n < N - 1:
            if board[h][n - 1]:
                n -= 1
            elif board[h][n]:
                n += 1
        else:
            if board[h][n - 1]:
                n -= 1
    if n == sp:
        return True
    else:
        return False


N, M, H = map(int, input().split())

board = [[0 for _ in range(N - 1)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

ans = 987654321

def backtracking(index, installed, board):
    def installable(h, n, board):
        if n == 0 and N - 1 > 1:
            if board[h][n + 1]:
                return False
        elif 0 < n < N - 2:
            if board[h][n - 1] or board[h][n + 1]:
                return False
        else:
            if board[h][n - 1]:
                return False
        return True

    global ans
    # print(f"[DEBUG] backtracking {index}, {installed}")

    if installed > 3 or installed > ans:
        return

    correct = True
    for i in range(N):
        if not simulation(i, board):
            correct = False
            break
    if correct:
        ans = min(ans, installed)
        return

    for curIndex in range(index, H * (N - 1)):
        h = curIndex // (N - 1)
        n = curIndex % (N - 1)
        if board[h][n] == 0 and installable(h, n, board):
            board[h][n] = 1
            backtracking(curIndex + 1, installed + 1, board)
            board[h][n] = 0


correct = True
for i in range(N):
    if not simulation(i, board):
        correct = False
        break
if correct:
    ans = min(ans, 0)
backtracking(0, 0, board)
if ans > 3:
    print("-1")
else:
    print(ans)



"""
for i in board:
    print(i)


print(simulation(0, 0, board))
print(simulation(0, 2, board))
"""


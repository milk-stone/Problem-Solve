import sys

input = sys.stdin.readline

N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]


white = 0
blue = 0


def solve(r, c, n):
    global white, blue
    if n == 1:
        if b[r][c] == 0:
            white += 1
        else:
            blue += 1
        return

    d = n // 2
    for sR, sC in [(r, c), (r, c + d), (r + d, c), (r + d, c + d)]:
        divide = False
        target = b[sR][sC]
        for i in range(sR, sR + d):
            for j in range(sC, sC + d):
                if b[i][j] != target:
                    divide = True
                    break
            if divide: break
        if not divide:
            if target == 0:
                white += 1
            else:
                blue += 1
        else:
            solve(sR, sC, d)

divide = False
target = b[0][0]
for i in range(N):
    for j in range(N):
        if b[i][j] != target:
            divide = True
            break
    if divide: break
if not divide:
    if target == 0:
        white += 1
    else:
        blue += 1
else:
    solve(0, 0, N)

print(white, blue, sep="\n")

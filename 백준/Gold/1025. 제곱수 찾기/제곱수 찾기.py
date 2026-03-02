import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

def isSquare(num):
    temp = int(num ** (0.5))
    if temp * temp == num:
        return True
    return False


dydx = []
for dy in range(N):
    for dx in range(M):
        if dy == 0 and dx == 0:
            dydx.append((dy, dx))
            continue
        dydx.append((dy, dx))
        dydx.append((dy, -dx))


maxValue = -1
for sy in range(N):
    for sx in range(M):
        for dy, dx in dydx:
            ny, nx = sy, sx
            s = board[sy][sx]
            if dy == 0 and dx == 0:
                s_int = int(s)
                if isSquare(s_int) and s_int > maxValue:
                    maxValue = s_int
                continue
            while True:
                s_int = int(s)
                if isSquare(s_int) and s_int > maxValue:
                    maxValue = s_int
                s_inverse = int(s[::-1])
                if isSquare(s_inverse) and s_inverse > maxValue:
                    maxValue = s_inverse

                ny += dy
                nx += dx
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    break
                s += board[ny][nx]

print(maxValue)

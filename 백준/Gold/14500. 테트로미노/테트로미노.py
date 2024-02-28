import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
maxValue = 0

# 2x2 (1 case)
for i in range(0, N-1):
    for j in range(0, M-1):
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i][j + 1] + a[i + 1][j + 1])
# 1x4 (1 case)
for i in range(0, N):
    for j in range(0, M-3):
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3])
# 4x1 (1 case)
for i in range(0, N-3):
    for j in range(0, M):
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j])
# 3x2 (8 case)
for i in range(0, N-2):
    for j in range(0, M-1):
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j + 1])
        maxValue = max(maxValue, a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1] + a[i + 2][j])
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 2][j])
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1])
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1])
        maxValue = max(maxValue, a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j])
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j])
        maxValue = max(maxValue, a[i + 1][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1])
# 2x3 (8 case)
for i in range(0, N-1):
    for j in range(0, M-2):
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2])
        maxValue = max(maxValue, a[i + 1][j] + a[i + 1][j + 1] + a[i][j + 1] + a[i][j + 2])
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1])
        maxValue = max(maxValue, a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2])
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 2])
        maxValue = max(maxValue, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j])
        maxValue = max(maxValue, a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2])
        maxValue = max(maxValue, a[i][j + 2] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2])
print(maxValue)
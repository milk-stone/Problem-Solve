import sys

input = sys.stdin.readline

N = int(input())
gboard_str = [list(input().strip()) for _ in range(N)]

rows = []
cols = []
gCount = 0

for i in range(N):
    for j in range(N):
        if gboard_str[i][j] == 'G':
            rows.append(i)
            cols.append(j)
            gCount += 1

if gCount <= 1:
    print(0)
    exit(0)

min_r, max_r = min(rows), max(rows)
min_c, max_c = min(cols), max(cols)

ans = 0

# 행(Row)이 다르다면(여러 행에 퍼져있다면) 위쪽 끝 vs 아래쪽 끝 중 가까운 곳으로 밈
if min_r != max_r:
    ans += min(max_r, N - 1 - min_r)

# 열(Col)이 다르다면(여러 열에 퍼져있다면) 왼쪽 끝 vs 오른쪽 끝 중 가까운 곳으로 밈
if min_c != max_c:
    ans += min(max_c, N - 1 - min_c)

print(ans)
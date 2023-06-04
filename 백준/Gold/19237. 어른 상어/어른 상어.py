import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
firstdir = list(map(int, input().split()))
for i in range(m):
    firstdir[i] -= 1
dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]# 1 2 3 4 위 아래 왼쪽 오른쪽
priority = [[] for _ in range(m+1)]# 상어 번호대로 넣을 것
for i in range(1, m+1):
    for j in range(4):
        arr = list(map(int, input().split()))
        for j in range(4):
            arr[j] -= 1
        priority[i].append(arr)

smell = [[[0, 0] for _ in range(n)] for _ in range(n)] # [상어 번호, 남은 시간]
sharkDead = [False for _ in range(m+1)]
empty = [[True for _ in range(n)] for _ in range(n)]

# 상어 시작 위치 저장
shark = [[0, 0, 0]]
for i in range(1, m+1):
    checked = False
    for y in range(n):
        for x in range(n):
            if a[y][x] == i:
                shark.append([y, x, firstdir[i-1]])
                smell[y][x] = [i, k]
                empty[y][x] = False
                checked = True
                break
        if checked:
            break

time = 0
while time <= 1000:
    # 종료 조건
    ended = True
    for i in range(2, m+1):
        if not sharkDead[i]:
            ended = False
        if not ended:
            break
    if ended:
        break
    # 상어의 이동
    for i in range(m, 0, -1):# 이동 할 상어 번호
        if sharkDead[i]:
            continue
        y, x, d = shark[i]
        moved = False
        for dir in priority[i][d]:
            dy, dx = dydx[dir]
            ny, nx = y + dy, x + dx
            # 이동 우선 순위 : 냄새 없는 칸 없을 시 내 냄새 칸
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if smell[ny][nx][0] == 0:
                smell[ny][nx] = [i, k+1]
                shark[i] = ny, nx, dir
                moved = True
            elif empty[ny][nx] and i < smell[ny][nx][0] and smell[ny][nx][1] == k+1:# 번호 작은 녀석이 먹습니다.
                shark[smell[ny][nx][0]] = 0, 0, 0 # 상어가 먹혔어요
                sharkDead[smell[ny][nx][0]] = True
                smell[ny][nx] = [i, k+1]
                shark[i] = ny, nx, dir
                moved = True
            if moved:
                break
        if moved:
            continue
        for dir in priority[i][d]:
            dy, dx = dydx[dir]
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if smell[ny][nx][0] == i:
                smell[ny][nx][1] = k+1
                shark[i] = ny, nx, dir
                moved = True
            if moved:
                break
    # 시간이 흐르면서 냄새가 1씩 줄어듭니다.
    time += 1
    for y in range(n):
        for x in range(n):
            if smell[y][x][1] > 1:
                smell[y][x][1] -= 1
                empty[y][x] = False
            elif smell[y][x][1] == 1:
                smell[y][x] = [0, 0]
                empty[y][x] = True
print(-1 if time > 1000 else time)

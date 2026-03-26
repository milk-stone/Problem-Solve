import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

def move(sr, sc, s, d):
    global drdc, R, C
    invertTable = {
        1: 2,
        2: 1,
        3: 4,
        4: 3,
    }

    moveCount = 0
    r, c = sr, sc
    if d <= 2: # 상하 이동
        while moveCount < s:
            dr, dc = drdc[d]
            if r + dr < 0 or r + dr >= R:
                d = invertTable[d]
                dr, dc = drdc[d]
            r += dr
            moveCount += 1
    else: # 좌우 이동
        while moveCount < s:
            dr, dc = drdc[d]
            if c + dc < 0 or c + dc >= C:
                d = invertTable[d]
                dr, dc = drdc[d]
            c += dc
            moveCount += 1
    return r, c, d



sharks = []
dot_to_shark = {}
# shark_to_dot = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split()) # r, c, 속력, 이동방향, 크기
    r -= 1
    c -= 1
    index = r * C + c
    dot_to_shark[index] = [s, d, z]
    # shark_to_dot[z] = dot_to_1d

# Phase 1. 낚시왕 한 칸 이동한 후 시작
personIndex = 0

fished = 0
drdc = [(-1, -1), (-1, 0), (1, 0), (0, 1), (0, -1)]

while personIndex < C:
    # Phase 2. 낚시왕의 낚시
    for i in range(R):
        if i * C + personIndex in dot_to_shark.keys():
            s, d, z = dot_to_shark.pop(i * C + personIndex)
            fished += z
            # shark_to_dot.pop(z)
            break

    # Phase 3. 상어의 이동
    # nextShark_to_dot = {}
    nextDot_to_shark = {}
    # print(f"FISHED = {fished}")
    # print(f"BEFORE MOVE : {dot_to_shark}")
    for index in dot_to_shark.keys():
        sr = index // C
        sc = index % C
        s, d, z = dot_to_shark[index]
        # print(f"before: s = {s}, d = {d}, ({sr}, {sc}) | ", end="")
        nr, nc, d = move(sr, sc, s, d)
        nextIndex = nr * C + nc
        # print(f"after: s = {s}, d = {d} | -> ({nr}, {nc})")
        if nextIndex not in nextDot_to_shark.keys():
            nextDot_to_shark[nextIndex] = [s, d, z]
            # nextShark_to_dot[z] = nextIndex
        else:
            if z > nextDot_to_shark[nextIndex][2]:
                nextDot_to_shark[nextIndex] = [s, d, z]
                # nextShark_to_dot[z] = nextIndex
    dot_to_shark = nextDot_to_shark

    # Phase 1. 낚시왕 한 칸 이동
    personIndex += 1
    # print(f"AFTER MOVE : {dot_to_shark}\n")
print(fished)

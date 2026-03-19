import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = deque([])

enlet = 0
outlet = N - 1

visited = [False for _ in range(2 * N)]
phase = 0
while True:
    # print(enlet, outlet, belt)
    # 4단계: 탈출 조건 확인
    count = 0
    for i in belt:
        if i == 0:
            count += 1
    if count >= K:
        break

    # 회차 시작
    phase += 1

    # 1단계: 벨트 회전
    enlet -= 1
    outlet -= 1
    if enlet < 0:
        enlet = 2 * N - 1
    if outlet < 0:
        outlet = 2 * N - 1

    if visited[outlet]:
        visited[outlet] = False
        if robots and robots[0] == outlet:
            robots.popleft()

    # 2단계: 로봇의 이동
    for _ in range(len(robots)):
        robot = robots.popleft()
        np = (robot + 1) % (2 * N)

        if not visited[np] and belt[np] > 0:
            visited[robot] = False
            belt[np] -= 1

            if np == outlet:
                pass
            else:
                visited[np] = True
                robots.append(np)

        else:
            robots.append(robot)

    # 3단계: 새로운 로봇 올리기
    if not visited[enlet] and belt[enlet] > 0:
        visited[enlet] = True
        belt[enlet] -= 1
        robots.append(enlet)

print(phase)
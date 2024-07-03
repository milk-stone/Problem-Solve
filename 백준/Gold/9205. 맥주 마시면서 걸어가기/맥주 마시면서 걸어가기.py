from collections import deque
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    sy, sx = map(int, input().split())
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    visited = [False for _ in range(len(store))]
    fy, fx = map(int, input().split())

    q = deque([[sy, sx]])
    found = False
    while q:
        y, x = q.popleft()
        if abs(fy - y) + abs(fx - x) <= 1000:
            found = True
            break
        for i in range(len(store)):
            dis = abs(store[i][0] - y) + abs(store[i][1] - x)
            if dis <= 1000 and not visited[i]:
                visited[i] = True
                q.append(store[i])

    if found:
        print("happy")
    else:
        print("sad")




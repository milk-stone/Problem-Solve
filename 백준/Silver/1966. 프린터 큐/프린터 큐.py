import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, targetIndex = map(int, input().split())
    l = []
    for i in list(map(int, input().split())):
        l.append([i, False])

    l[targetIndex][1] = True

    q = deque(l)

    printed = 0
    while True:
        now = q.popleft()

        printable = True
        for follower in q:
            if now[0] < follower[0]:
                q.append(now)
                printable = False
                break
        
        if printable:
            printed += 1
            if now[1]:
                print(printed)
                break




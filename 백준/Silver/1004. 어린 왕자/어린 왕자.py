import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    S = int(input())
    count = 0
    for __ in range(S):
        a, b, r = map(int, input().split())
        first = False
        if (x1 - a) ** 2 + (y1 - b) ** 2 < r ** 2:
            first = True
        second = False
        if (x2 - a) ** 2 + (y2 - b) ** 2 < r ** 2:
            second = True
        if (first and not second) or (not first and second):
            count += 1
    print(count)
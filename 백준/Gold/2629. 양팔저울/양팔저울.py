import sys

input = sys.stdin.readline

n = int(input())
chu = list(map(int, input().split()))
k = int(input())
things = list(map(int, input().split()))
dp = set()
new = []
for i in range(n):
    new = []
    for j in dp:
        for k in [j - chu[i], j + chu[i], chu[i] - j]:
            if 1 <= k < 40001 and k not in dp:
                new.append(k)
    for j in new:
        dp.add(j)
    if chu[i] not in dp:
        dp.add(chu[i])
for i in things:
    if i in dp:
        print("Y", end=' ')
    else:
        print("N", end=' ')

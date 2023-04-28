import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(2)]
costs = sum(data[1])
trans = [tuple(x) for x in zip(*data)]

a = [0 for _ in range(costs+1)]
for i in range(N):
    byte, cost = trans[i]
    b = [0 for _ in range(costs+1)]
    for j in range(costs+1):
        if j >= cost:
            b[j] = max(a[j], a[j-cost] + byte)
        else:
            b[j] = a[j]
    a = b

for i in range(costs + 1):
    if a[i] >= M:
        print(i)
        break
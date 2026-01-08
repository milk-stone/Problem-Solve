import math
import sys

input = sys.stdin.readline

N = int(input())

minNode = [40001, 40001]
store = []
for _ in range(N):
    x, y = map(int, input().split())
    if minNode[1] > y:
        minNode = [x, y]
    elif minNode[1] == y:
        if minNode[0] < x:
            minNode = [x, y]
    store.append([x, y, 0, 0])

# Calculate Angles
for i in range(N):
    if store[i][0] == minNode[0] and store[i][1] == minNode[1]:
        store[i][2] = -181
        continue
    store[i][2] = math.atan2(store[i][1] - minNode[1], store[i][0] - minNode[0])
    store[i][3] = (store[i][1] - minNode[1]) ** 2 + (store[i][0] - minNode[0]) ** 2

# Sort
store.sort(key=lambda x: (x[2], x[3]))


def ccw(i, j, k):
    area = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area > 0:
        return True
    return False


gramScan = []
gramScan.append(store[0])
gramScan.append(store[1])

for i in range(2, N):
    while len(gramScan) >= 2:
        second = gramScan.pop()
        first = gramScan[-1]
        if ccw(first, second, store[i]):
            gramScan.append(second)
            break
    gramScan.append(store[i])

if not ccw(gramScan[-2], gramScan[-1], store[0]):
    gramScan.pop()

print(len(gramScan))

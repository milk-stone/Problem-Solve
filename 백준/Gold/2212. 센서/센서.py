import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

interval = []

for i in range(N):
    interval.append([arr[i], arr[i]])

ans = 0
while len(interval) > K:
    minCount = 1_000_001
    left, right = -1, -1
    for i in range(1, len(interval)):
        v = interval[i][0] - interval[i - 1][1]
        if v < minCount:
            minCount = v
            left, right = i - 1, i

    ans += minCount

    new_interval = []
    for i in range(len(interval)):
        if i == left:
            new_interval.append([interval[left][0], interval[right][1]])
        elif i == right:
            continue
        else:
            new_interval.append(interval[i])
    interval = new_interval

print(ans)

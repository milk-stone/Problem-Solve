import sys

input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    lines.append(tuple(map(int, input().split())))

lines.sort(key=lambda x: x[0])

ans = 0
start, end = -1000000001, -1000000001

for x, y in lines:
    if x > end:
        ans += end - start
        start, end = x, y
    if y > end:
        end = y
ans += end - start
print(ans)

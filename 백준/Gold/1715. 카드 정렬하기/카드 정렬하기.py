import sys
import heapq

input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    item = int(input())
    heapq.heappush(h, item)

ans = 0
while True:
    if len(h) < 2:
        break
    item1 = heapq.heappop(h)
    item2 = heapq.heappop(h)
    heapq.heappush(h, item1 + item2)
    ans += item1 + item2

print(ans)
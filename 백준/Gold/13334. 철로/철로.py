import heapq
import sys

input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    a, b = map(int, input().split())
    l.append((min(a, b), max(a, b)))
L = int(input())

l.sort(key=lambda x: x[1])

pq = []
ans = 0
for a, b in l:
    if b - a > L:
        continue

    heapq.heappush(pq, a)

    while pq and b - pq[0] > L:
        heapq.heappop(pq)

    ans = max(ans, len(pq))
print(ans)

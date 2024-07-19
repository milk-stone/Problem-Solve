import heapq
import sys

input = sys.stdin.readline

N = int(input())
h = []
lectures = [tuple(map(int, input().split())) for _ in range(N)]
rooms = 0

lectures.sort()

for a, b in lectures:
    if len(h) == 0:
        heapq.heappush(h, b)
        rooms += 1
        continue
    if h[0] > a:
        heapq.heappush(h, b)
        rooms += 1
    else:
        heapq.heappop(h)
        heapq.heappush(h, b)
print(rooms)

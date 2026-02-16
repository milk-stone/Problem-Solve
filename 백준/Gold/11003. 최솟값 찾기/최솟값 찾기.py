import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
ans = []
for i in range(N):
    curValue = arr[i]
    while q and q[-1][1] > curValue:
        q.pop()

    q.append((i, curValue))
    if q[0][0] <= i - L:
        q.popleft()

    ans.append(q[0][1])
print(*ans)

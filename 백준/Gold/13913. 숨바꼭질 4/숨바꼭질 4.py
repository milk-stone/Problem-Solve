from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = 0
    while q:
        now = q.popleft()
        if now == k:
            return
        for i in [now + 1, now - 1, now*2]:
            if 0 <= i <= 100000:
                if visited[i] == -1:
                    visited[i] = visited[now] + 1
                    route[i] = now
                    q.append(i)


n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
route = {}
bfs(n)
print(visited[k])
ans = []
temp = k
while temp != n:
    ans.append(temp)
    temp = route[temp]
ans.append(temp)
ans.reverse()
print(*ans)

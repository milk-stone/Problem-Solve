from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False for _ in range(N+1)]

q = deque([1])
visited[1] = True
ans = [-1 for _ in range(N+1)]

while q:
    now = q.popleft()
    for nextNode in G[now]:
        if not visited[nextNode]:
            q.append(nextNode)
            ans[nextNode] = now
            visited[nextNode] = True

for i in range(2, N+1):
    print(ans[i])
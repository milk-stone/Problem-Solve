import sys
from collections import deque

input = sys.stdin.readline

N, M, Q = map(int, input().split())
g = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)

# 미리 BFS를 돌려서 메모이제이션을 해보자
dist = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

minValue = 987654321
for start in range(1, N + 1):
    visited = [False] * (N + 1)
    q = deque([(start, 0)])
    while q:
        now, distance = q.popleft()
        dist[start][now] = distance
        for nextNode in g[now]:
            if not visited[nextNode]:
                visited[nextNode] = True
                q.append((nextNode, distance + 1))


for _ in range(Q):
    a, b = map(int, input().split())
    minValue = 987654321
    for i in range(1, N + 1):
        if dist[i][a] == -1 or dist[i][b] == -1:
            continue
        d = max(dist[i][a], dist[i][b])
        if d != -1:
            minValue = min(minValue, d)
    if minValue == 987654321:
        print("-1")
    else:
        print(f"{minValue}")


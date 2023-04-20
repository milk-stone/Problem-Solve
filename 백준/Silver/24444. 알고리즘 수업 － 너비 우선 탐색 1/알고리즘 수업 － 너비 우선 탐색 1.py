from collections import deque
import sys

input = sys.stdin.readline

N, M, start = map(int, input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1):
    graph[i].sort()
q = deque([start])
count = 1
visited[start] = 1
count += 1
while q:
    now = q.popleft()
    for next in graph[now]:
        if visited[next] == 0:
            q.append(next)
            visited[next] = count
            count += 1
for i in range(1, N+1):
    print(visited[i])

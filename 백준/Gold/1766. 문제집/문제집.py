import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = []
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)
        visited[i] = True


while q:
    now = heapq.heappop(q)
    ans.append(now)
    for nextValue in graph[now]:
        inDegree[nextValue] -= 1

    for i in range(1, n+1):
        if not visited[i] and inDegree[i] == 0:
            heapq.heappush(q, i)
            visited[i] = True

print(*ans)
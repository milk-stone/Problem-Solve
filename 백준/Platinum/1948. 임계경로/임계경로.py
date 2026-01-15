import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
M = int(input())

g = [[] for _ in range(N + 1)]
g_i = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)

for _ in range(M):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g_i[b].append((a, w))
    indegree[b] += 1

start, end = map(int, input().split())

q = deque([start])
maxTime = [0 for _ in range(N + 1)]


while q:
    now = q.popleft()
    for nextNode, weight in g[now]:
        if maxTime[nextNode] < maxTime[now] + weight:
            maxTime[nextNode] = maxTime[now] + weight
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            q.append(nextNode)

print(maxTime[end])

r_visited = [False for _ in range(N + 1)]
r_visited[end] = True
maxRoad = 0

def rdfs(now):
    global maxRoad
    for nextNode, weight in g_i[now]:
        if maxTime[now] - weight == maxTime[nextNode]:
            if r_visited[nextNode]:
                maxRoad += 1
                continue
            if not r_visited[nextNode]:
                r_visited[nextNode] = True
                maxRoad += 1
                rdfs(nextNode)


rdfs(end)

print(maxRoad)
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for next in graph[start]:
        if not visited[next]:
            dfs(next)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort()
visited = [0 for _ in range(n+1)]
cnt = 1
dfs(r)
for i in range(1, n+1):
    print(visited[i])
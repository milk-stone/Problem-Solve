import sys

sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def dfs(start, cur_depth):
    visited[start] = True
    depth[start] = cur_depth
    for i in g[start]:
        if not visited[i]:
            parent[i] = start
            dfs(i, cur_depth + 1)


def lca(a, b):
    while depth[a] > depth[b]:
        a = parent[a]
    while depth[b] > depth[a]:
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
visited = [False] * (N + 1)
depth = [0] * (N + 1)
parent = [0] * (N + 1)
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1, 0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
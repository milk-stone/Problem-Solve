import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

V, E = map(int, input().split())

g = [[] for _ in range(V + 1)]
g_inverse = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    g[a].append(b)
    g_inverse[b].append(a)


def dfs(start, g, l, visited):
    for i in g[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, g, l, visited)
    l.append(start)


visited = [False for _ in range(V + 1)]
reverseList = []
for i in range(1, V + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i, g_inverse, reverseList, visited)

reverseList.reverse()

result = []

visited = [False for _ in range(V + 1)]
for i in reverseList:
    if not visited[i]:
        scc = []
        visited[i] = True
        dfs(i, g, scc, visited)
        scc.sort()
        result.append(scc)

result.sort()

print(len(result))
for row in result:
    for item in row:
        print(item, end=" ")
    print("-1")

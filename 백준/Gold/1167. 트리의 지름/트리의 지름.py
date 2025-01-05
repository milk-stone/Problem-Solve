import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(start, weight):
    global maxWeight, lastNode, visited, g
    visited[start] = True

    for nextNode, w in g[start]:
        if not visited[nextNode]:
            dfs(nextNode, weight + w)

    if weight > maxWeight:
        maxWeight = weight
        lastNode = start



V = int(input())

g = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

for _ in range(V):
    temp = list(map(int, input().split()))
    index = 1
    while temp[index] != -1:
        g[temp[0]].append((temp[index], temp[index + 1]))
        index += 2

maxWeight = -1
lastNode = -1

dfs(1, 0)
# print(maxWeight, lastNode, visited)

visited = [False for _ in range(V+1)]
maxWeight = -1
dfs(lastNode, 0)
# print(maxWeight, lastNode, visited)

print(maxWeight)


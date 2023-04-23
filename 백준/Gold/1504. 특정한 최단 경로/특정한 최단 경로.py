import sys

input = sys.stdin.readline

INF = 987654321

def getSmallestIndex(index):
    minValue = INF
    minIndex = 0
    for i in range(1, V+1):
        if not visited[i] and minValue > distance[index][i]:
            minValue = distance[index][i]
            minIndex = i
    return minIndex

def dijkstra(start, index):
    distance[index][start] = 0
    visited[start] = True
    for i in graph[start]:
        if distance[index][i[0]] > i[1]:
            distance[index][i[0]] = i[1]
    for _ in range(V+1):
        now = getSmallestIndex(index)
        visited[now] = True
        for next in graph[now]:
            cost = distance[index][now] + next[1]
            if cost < distance[index][next[0]]:
                distance[index][next[0]] = cost


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())
distance = [[INF for _ in range(V+1)] for _ in range(3)]
visited = [False for _ in range(V+1)]
dijkstra(1, 0)
visited = [False for _ in range(V+1)]
dijkstra(v1, 1)
visited = [False for _ in range(V+1)]
dijkstra(v2, 2)

a = distance[0][v1] + distance[1][v2] + distance[2][V]
b = distance[0][v2] + distance[1][V] + distance[2][v1]
if a >= INF or b >= INF:
    print(-1)
else:
    print(min(a, b))

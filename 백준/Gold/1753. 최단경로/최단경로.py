import sys

input = sys.stdin.readline

INF = 987654321

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
visited = [False]*(v+1)

for i in range(e):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def getSmallestIndex():
	minValue = INF
	index = 0
	for i in range(1, v+1):
		if not visited[i] and distance[i] < minValue:
			minValue = distance[i]
			index = i
	return index

def dijkstra(start):
	distance[start] = 0
	visited[start] = True
	for i in graph[start]:
		if distance[i[0]] >= i[1]:
			distance[i[0]] = i[1]
	for _ in range(v-1):
		now = getSmallestIndex()
		visited[now] = True
		for next in graph[now]:
			cost = distance[now] + next[1]
			if cost < distance[next[0]]:
				distance[next[0]] = cost

dijkstra(start)
for i in range(1, v+1):
	if distance[i] == INF:
		print('INF')
	else:
		print(distance[i])
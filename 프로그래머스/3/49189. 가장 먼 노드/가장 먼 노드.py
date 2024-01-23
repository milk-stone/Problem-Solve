from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = [0 for _ in range(len(edge) + 1)]
    start = 1
    visited = [False for _ in range(n+1)]
    visited[start] = True
    q = deque([(start, 0)])
    maxValue = 0
    while q:
        now, count = q.popleft()
        for nextNode in graph[now]:
            if not visited[nextNode]:
                visited[nextNode] = True
                q.append((nextNode, count + 1))
                distance[count + 1] += 1
                maxValue = count + 1
    
    answer = distance[maxValue]
    
    
    return answer
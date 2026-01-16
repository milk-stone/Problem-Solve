def solution(n, results):
    from collections import deque
    
    def bfs(start):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        
        count = 1
        while q:
            now = q.popleft()
            for nextNode in g[now]:
                if not visited[nextNode]:
                    visited[nextNode] = True
                    q.append(nextNode)
                    count += 1
        return count
        
        
    def rbfs(start):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        
        count = 1
        while q:
            now = q.popleft()
            for nextNode in g_i[now]:
                if not visited[nextNode]:
                    visited[nextNode] = True
                    q.append(nextNode)
                    count += 1
        return count
    
    g = [[] for _ in range(n + 1)]
    g_i = [[] for _ in range(n + 1)]
    
    for a, b in results:
        g[a].append(b)
        g_i[b].append(a)
    
    answer = 0
    for i in range(1, n + 1):
        if bfs(i) + rbfs(i) == n + 1:
            answer += 1
    return answer
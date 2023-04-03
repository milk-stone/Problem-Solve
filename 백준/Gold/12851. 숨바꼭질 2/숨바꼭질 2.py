from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    count = 0
    q = deque([start])
    visited[start][0] = 0
    visited[start][1] = 1
    while q:
        now = q.popleft()
        for i in [now - 1, now + 1, now * 2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[now][0] + 1
                    visited[i][1] = visited[now][1]
                    q.append(i)
                elif visited[i][0] == visited[now][0] + 1:
                    visited[i][1] += visited[now][1]


n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
bfs(n)
print(visited[k][0])
print(visited[k][1])

import sys
import bisect

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def dfs(start):
    global G, visited, path
    visited[start] = True
    path.append(start)
    for nextNode in G[start]:
        if not visited[nextNode]:
            dfs(nextNode)
    return

def lis_length(seq):
    dp = []
    for a in seq:
        pos = bisect.bisect_left(dp, a)
        if pos == len(dp):
            dp.append(a)
        else:
            dp[pos] = a
    return len(dp)


V = int(input())
if V <= 2:
    print(-1)
    exit(0)

G = [[] for _ in range(V+1)]
for v in range(1, V + 1):
    left, right = map(int, input().split())
    G[v].append(left)
    G[v].append(right)


ans = -1
for start in range(1, V+1):
    for index in [0, 1]:
        visited = [False for _ in range(V + 1)]
        visited[start] = True
        path = [start]
        dfs(G[start][index])

        t = lis_length(path)
        if len(path) != V:
            print(-1)
            exit(0)
        if t > ans: ans = t
        # print(path)
        path.reverse()
        # print(path)

        t = lis_length(path)
        if len(path) != V:
            print(-1)
            exit(1)
        if t > ans: ans = t

print(V - ans)
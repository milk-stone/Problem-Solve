import sys

input = sys.stdin.readline


def bf(start):
    dist = [987654321 for _ in range(N + 1)]
    dist[start] = 0
    for i in range(N):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N - 1:
                    return True
    return False

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(W):
        a, b, c = map(int, input().split())
        edges.append((b, a, -c))

    if bf(1):
        print("YES")
    else:
        print("NO")
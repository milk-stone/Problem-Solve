import sys

input = sys.stdin.readline

V = int(input())

G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]
for i in range(1, V+1):
    G[i][i] = 0

E = int(input())
for _ in range(E):
    origin, dest, weight = map(int, input().split())
    G[origin][dest] = min(G[origin][dest], weight)

for via in range(1, V+1): # via 번 정점을 거쳐간다
    for origin in range(1, V+1):
        if via == origin:
            continue
        for dest in range(1, V+1):
            if origin == dest or via == dest:
                continue
            G[origin][dest] = min(G[origin][dest], G[origin][via] + G[via][dest])


for i in range(1, V+1):
    for j in range(1, V+1):
        print(0 if G[i][j] >= 987654321 else G[i][j], end=' ')
    print()
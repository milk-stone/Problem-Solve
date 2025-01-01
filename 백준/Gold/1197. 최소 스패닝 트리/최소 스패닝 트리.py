import sys

input = sys.stdin.readline
v, e = map(int, input().split())
eList = [tuple(map(int, input().split())) for _ in range(e)]
eList.sort(key = lambda x: x[2])
parent = [i for i in range(v+1)]
size = [1 for i in range(v+1)]


def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    if size[a] > size[b]:
        parent[b] = a
        size[a] += size[b]
    else:
        parent[a] = b
        size[b] += size[a]


answer = 0
for a, b, cost in eList:
    a = find(a)
    b = find(b)
    if a != b:
        answer += cost
        union(a, b)
print(answer)
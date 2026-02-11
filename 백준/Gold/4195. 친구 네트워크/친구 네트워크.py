import sys

input = sys.stdin.readline

parent = {}
size = {}

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        if size[rootA] < size[rootB]:
            parent[rootA] = rootB
            size[rootB] += size[rootA]
            print(size[rootB])
            return
        else:
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            print(size[rootA])
            return
    print(size[rootA])
    return

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    size = {}
    for __ in range(F):
        a, b = input().strip().split()

        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1

        union(a, b)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [x for x in range(n+1)]
ans = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    s1 = find(a)
    s2 = find(b)
    if s1 != s2:
        parent[s2] = s1


for _ in range(m):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        if find(arr[1]) == find(arr[2]):
            ans.append("YES")
        else:
            ans.append("NO")
    elif arr[0] == 0:
        if arr[1] != arr[2]:
            union(arr[1], arr[2])

for i in ans:
    print(i)
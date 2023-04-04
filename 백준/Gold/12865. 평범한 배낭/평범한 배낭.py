import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = [0 for _ in range(k+1)]
w, v = map(int ,input().split())
for i in range(w, k+1):
    a[i] = v
b = [0 for _ in range(k+1)]
for _ in range(n-1):
    w, v = map(int ,input().split())
    for i in range(min(w, k+1)):
        b[i] = a[i]
    for i in range(w, k+1):
        b[i] = max(a[i], a[i-w] + v)
    a = b
    b = [0 for _ in range(k+1)]
print(a[-1])

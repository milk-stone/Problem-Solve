import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a, b + 1):
        arr[i - 1] = c
for i in arr:
    print(i, end=" ")
print()

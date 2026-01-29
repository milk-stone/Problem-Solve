import sys

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

selected = []
selected.append(arr[0])

for i in range(1, N):
    if selected[-1][1] <= arr[i][0]:
        selected.append(arr[i])

print(len(selected))
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

dist = []
for i in range(1, N):
    dist.append(arr[i] - arr[i - 1])

dist.sort(reverse=True)
print(sum(dist[K - 1:]))

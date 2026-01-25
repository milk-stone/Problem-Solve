import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
for i in range(N - 1, -1, -1):
    while K >= coins[i]:
        K -= coins[i]
        count += 1
    if K == 0:
        break
print(count)
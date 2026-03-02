import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
temp = 0
for i in range(N):
    temp += arr[i]
    sum_arr.append(temp)

for _ in range(M):
    a, b = map(int, input().split())
    print(sum_arr[b] - sum_arr[a - 1])
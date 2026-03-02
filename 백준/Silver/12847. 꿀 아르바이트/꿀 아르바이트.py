import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
temp = 0
for i in range(N):
    temp += arr[i]
    sum_arr.append(temp)

maxValue = -1
for i in range(M, N):
    cur = sum_arr[i] - sum_arr[i - M]
    if cur > maxValue:
        maxValue = cur
print(maxValue)
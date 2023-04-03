import sys

input = sys.stdin.readline


n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    minValue = 987654321
    for j in range(1, int(i**(1/2))+1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)
print(dp[n])
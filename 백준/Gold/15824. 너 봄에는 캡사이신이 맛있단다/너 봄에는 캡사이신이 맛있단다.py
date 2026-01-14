import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
MOD = 1_000_000_007
for i in range(N):
    maxCount = pow(2, i, MOD)
    minCount = pow(2, N - 1 - i, MOD)
    ans += (maxCount - minCount) * l[i]
    ans %= MOD
print(ans)

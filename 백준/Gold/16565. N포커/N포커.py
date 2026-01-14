import sys

input = sys.stdin.readline

N = int(input())

mem_ncr = [[-1 for _ in range(53)] for _ in range(53)]


def ncr(n, r):
    r = min(r, n - r)
    if mem_ncr[n][r] != -1:
        return mem_ncr[n][r]
    if n == r:
        return 1
    if r == 1:
        return n
    if r == 0:
        return 1
    mem_ncr[n][r] = (ncr(n - 1, r - 1) + ncr(n - 1, r))
    return mem_ncr[n][r]


MOD = 10_007
ans = 0
for i in range(1, N // 4 + 1):  # i 는 종류
    result = ncr(13, i) * ncr(52 - 4 * i, N - 4 * i)
    if i % 2:
        ans += result % MOD
    else:
        ans -= result % MOD
    ans %= MOD
print(ans)
import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for window_gap in range(1, N):
    inner = window_gap - 1
    factor = 2 ** inner
    for i in range(N - window_gap):
        ans += ((l[i + window_gap] - l[i]) * factor)
    ans %= 1_000_000_007
print(ans)

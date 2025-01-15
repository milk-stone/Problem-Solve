import sys
import bisect

input = sys.stdin.readline


def lis_length(seq):
    dp = []
    for a in seq:
        pos = bisect.bisect_left(dp, a)
        if pos == len(dp):
            dp.append(a)
        else:
            dp[pos] = a
    return len(dp)

N = int(input())
l = list(map(int, input().split()))
print(lis_length(l))
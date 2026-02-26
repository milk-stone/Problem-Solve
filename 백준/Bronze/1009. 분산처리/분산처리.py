import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    ans = a
    for i in range(b - 1):
        ans *= a
        ans %= 10
    ans %= 10
    print(ans if ans != 0 else 10)
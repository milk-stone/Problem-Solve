import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    count = 0
    N -= M * K
    count += 1
    if M * K == 1 and N > 0:
        print(-1)
        continue
    if N > 0:
        if N % (M * K - 1):
            count += ((N // (M * K - 1)) + 1) * 2
        else:
            count += ((N // (M * K - 1))) * 2
    print(count)
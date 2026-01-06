import sys

input = sys.stdin.readline

N = int(input())
phi = N

for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        while N % i == 0:
            N //= i
        phi //= i
        phi *= (i - 1)

if N > 1:
    phi //= N
    phi *= (N - 1)
print(phi)

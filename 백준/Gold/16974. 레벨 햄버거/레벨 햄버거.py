import sys

input = sys.stdin.readline

N, X = map(int, input().split())

n = 1
burger_count = 1
burger_mem = [0 for _ in range(50 + 1)]
burger_mem[0] = burger_count

beef_count = 1
beef_mem = [0 for _ in range(50 + 1)]
beef_mem[0] = beef_count

while n <= N:
    burger_count = 2 * burger_count + 3
    burger_mem[n] = burger_count
    beef_count = 2 * beef_count + 1
    beef_mem[n] = beef_count
    n += 1

sp = 1
ans = 0
while N >= 0:
    N -= 1
    if sp + burger_mem[N] < X:
        ans += beef_mem[N] + 1
        sp += burger_mem[N] + 1
        N += 1
    elif sp + burger_mem[N] == X:
        ans += beef_mem[N]
        sp += burger_mem[N]
        N += 1
    else:
        sp += 1
print(ans)


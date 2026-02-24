import sys

input = sys.stdin.readline

N, K, A = map(int, input().split())
minTime = 987654321
for _ in range(N):
    t, s = map(int, input().split())
    time = 0
    toDrink = K
    ended = False
    while True:
        for _ in range(t):
            toDrink -= A
            time += 1
            if toDrink <= 0:
                ended = True
                break
        if ended:
            break
        time += s
    minTime = min(minTime, time)
print(minTime)
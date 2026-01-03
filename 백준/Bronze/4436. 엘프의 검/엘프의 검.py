import sys

for line in sys.stdin:
    N = int(line.strip())
    visited = [False for _ in range(10)]
    k = 1
    while True:
        target = N * k
        while True:
            if target >= 10:
                visited[target % 10] = True
                target //= 10
            else:
                visited[target] = True
                break
        gameover = True
        for i in range(10):
            if not visited[i]:
                gameover = False
        if gameover:
            break
        k += 1
    print(k)

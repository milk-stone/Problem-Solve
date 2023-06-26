def solution(n):
    answer = [[-1 for _ in range(n)] for _ in range(n)]
    dydx = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    start = 1
    sy, sx, d = 0, 0, 0
    answer[sy][sx] = start
    
    while True:
        dy, dx = dydx[d]
        ny, nx = sy + dy, sx + dx
        if 0 <= ny < n and 0 <= nx < n and answer[ny][nx] == -1:
            start += 1
            answer[ny][nx] = start
            sy, sx = ny, nx
            continue
        else:
            d += 1
            if d > 3:
                d -= 4
        ended = True
        for a in range(n):
            for b in range(n):
                if answer[a][b] == -1:
                    ended = False
                    break
            if not ended:
                break
        if ended:
            break

    return answer

print(solution(4))
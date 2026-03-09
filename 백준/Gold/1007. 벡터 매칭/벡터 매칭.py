import sys

input = sys.stdin.readline

minDistance = float('inf')
def cal(vector_x, vector_y, curIndex, dots, plusCount, minusCount, N):
    # print(f"[DEBUG] {vector}, {curIndex}, {dots}, {plusCount, minusCount, N}")
    global minDistance
    if plusCount < N // 2:
        cal(vector_x + dots[curIndex + 1][0], vector_y + dots[curIndex + 1][1], curIndex + 1, dots, plusCount + 1, minusCount, N)
    if minusCount < N // 2:
        cal(vector_x - dots[curIndex + 1][0], vector_y - dots[curIndex + 1][1], curIndex + 1, dots, plusCount, minusCount + 1, N)
    if plusCount + minusCount == N:
        curDistance = (vector_x ** 2 + vector_y ** 2) ** (0.5)
        if curDistance < minDistance:
            minDistance = curDistance

T = int(input())
for _ in range(T):
    minDistance = float('inf')
    N = int(input())
    dots = []
    for __ in range(N):
        dots.append(list(map(int, input().split())))

    cal(dots[0][0], dots[0][1], 0, dots, 1, 0, N)

    print(minDistance)


